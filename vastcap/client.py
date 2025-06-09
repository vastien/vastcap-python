from __future__ import annotations

import asyncio
import time
from typing import Optional, Union, Any, TypeVar
from functools import wraps
import aiohttp
import requests
from .types import (
    BaseTask, TaskStatus, TaskSolution, SolverError,
    JsonDict
)
from .exceptions import ERROR_MAPPING, VastCapException

T = TypeVar("T")

class BaseClient:
    API_BASE_URL: str = "https://captcha.vast.sh/api/solver"
    DEFAULT_TIMEOUT: float = 120.0
    DEFAULT_POLLING: float = 3.0

    def __init__(
        self,
        api_key: str,
        timeout: float = DEFAULT_TIMEOUT,
        polling: float = DEFAULT_POLLING
    ) -> None:
        self.api_key = api_key
        self.timeout = timeout
        self.polling = polling

    def _handle_error(self, response_data: JsonDict) -> None:
        if error := response_data.get("error"):
            error_code = error.get("errorCode", "Unknown error")

            if exception_class := ERROR_MAPPING.get(error_code):
                raise exception_class
                
            raise VastCapException(
                error.get("errorDescription", "Unknown error"),
                error_code
            )

class Vast(BaseClient):
    def __post(self, endpoint: str, data: JsonDict) -> JsonDict:
        response = requests.post(
            f"{self.API_BASE_URL}/{endpoint}",
            json={"clientKey": self.api_key, **data},
            timeout=self.timeout
        )
        response_data = response.json()
        self._handle_error(response_data)
        return response_data

    def create_task(self, task: BaseTask) -> str:
        response = self.__post("createTask", {"task": task.to_dict()})
        return response["taskId"]

    def get_task_result(self, task_id: str) -> tuple[TaskStatus, Optional[Union[TaskSolution, SolverError]]]:
        response = self.__post("getTaskResult", {"taskId": task_id})
        status = TaskStatus(response["status"])
        
        match status:
            case TaskStatus.READY:
                return status, TaskSolution.from_dict(response["solution"])

            case TaskStatus.FAILED:
                return status, SolverError.from_dict(response["error"])

            case _:
                return status, None

    def get_balance(self) -> float:
        response = self.__post("getBalance", {})
        return float(response["balance"])

    def solve(
        self,
        task: BaseTask,
        timeout: Optional[float] = None,
        polling: Optional[float] = None
    ) -> TaskSolution:
        timeout = timeout or self.timeout
        polling = polling or self.polling
        end = time.time() + timeout
        task_id = self.create_task(task)

        while time.time() < end:
            status, result = self.get_task_result(task_id)

            match status:
                case TaskStatus.READY:
                    return result  # type: ignore

                case TaskStatus.FAILED:
                    raise VastCapException(str(result))

            time.sleep(polling)
        
        raise TimeoutError(f"Task {task_id} timed out after {timeout} seconds")

class AsyncVast(BaseClient):
    def __init__(
        self,
        api_key: str,
        timeout: float = BaseClient.DEFAULT_TIMEOUT,
        polling: float = BaseClient.DEFAULT_POLLING,
        session: Optional[aiohttp.ClientSession] = None
    ) -> None:
        super().__init__(api_key, timeout, polling)
        self._session = session

    async def __aenter__(self) -> AsyncVast:
        if not self._session:
            self._session = aiohttp.ClientSession()

        return self

    async def __aexit__(self, *_: Any) -> None:
        if self._session:
            await self._session.close()

    async def __post(self, endpoint: str, data: JsonDict) -> JsonDict:
        if not self._session:
            raise RuntimeError("Session not initialized. Use async with statement")
            
        async with self._session.post(
            f"{self.API_BASE_URL}/{endpoint}",
            json={"clientKey": self.api_key, **data},
            timeout=self.timeout
        ) as response:
            response_data = await response.json()
            self._handle_error(response_data)
            return response_data

    async def create_task(self, task: BaseTask) -> str:
        response = await self.__post("createTask", {"task": task.to_dict()})
        return response["taskId"]

    async def get_task_result(
        self,
        task_id: str
    ) -> tuple[TaskStatus, Optional[Union[TaskSolution, SolverError]]]:
        response = await self.__post("getTaskResult", {"taskId": task_id})
        status = TaskStatus(response["status"])
        
        match status:
            case TaskStatus.READY:
                return status, TaskSolution.from_dict(response["solution"])

            case TaskStatus.FAILED:
                return status, SolverError.from_dict(response["error"])

            case _:
                return status, None

    async def get_balance(self) -> float:
        response = await self.__post("getBalance", {})
        return float(response["balance"])

    async def solve(
        self,
        task: BaseTask,
        timeout: Optional[float] = None,
        polling: Optional[float] = None
    ) -> TaskSolution:
        timeout = timeout or self.timeout
        polling = polling or self.polling
        end = time.time() + timeout
        task_id = await self.create_task(task)

        while time.time() < end:
            status, result = await self.get_task_result(task_id)

            match status:
                case TaskStatus.READY:
                    return result  # type: ignore

                case TaskStatus.FAILED:
                    raise VastCapException(str(result))

            await asyncio.sleep(polling)
        
        raise TimeoutError(f"Task {task_id} timed out after {timeout} seconds")
