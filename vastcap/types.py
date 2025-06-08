from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional, Union, Dict, Any, TypeVar
from typing_extensions import TypeAlias

T = TypeVar("T", bound="BaseTask")
JsonDict: TypeAlias = Dict[str, Any]

class TaskType(str, Enum):
    RECAPTCHA_V2 = "RecaptchaV2Task"
    RECAPTCHA_V3 = "RecaptchaV3Task"
    HCAPTCHA = "HCaptchaTask"
    TURNSTILE = "TurnstileTask"
    FUNCAPTCHA = "FunCaptchaTask"

class TaskStatus(str, Enum):
    PROCESSING = "processing"
    READY = "ready"
    FAILED = "failed"

@dataclass 
class SolverError:
    error_id: int
    error_code: str
    error_description: str

    @classmethod
    def from_dict(cls, data: JsonDict) -> SolverError:
        return cls(
            error_id=data["errorId"],
            error_code=data["errorCode"],
            error_description=data["errorDescription"]
        )

@dataclass
class TaskSolution:
    grecaptcha_response: Optional[str] = None
    hcaptcha_response: Optional[str] = None
    turnstile_response: Optional[str] = None
    funcaptcha_response: Optional[str] = None
    score: Optional[float] = None
    user_agent: Optional[str] = None

    @classmethod
    def from_dict(cls, data: JsonDict) -> TaskSolution:
        return cls(
            grecaptcha_response=data.get("gRecaptchaResponse"),
            hcaptcha_response=data.get("hCaptchaResponse"),
            turnstile_response=data.get("turnstileResponse"),
            funcaptcha_response=data.get("token"),
            score=data.get("score"),
            user_agent=data.get("userAgent")
        )

@dataclass
class BaseTask:
    type: TaskType
    website_url: str
    website_key: str
    user_agent: Optional[str] = None
    proxy: Optional[str] = None

    def to_dict(self) -> JsonDict:
        return {k: v for k, v in {
            "type": self.type.value,
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
            "userAgent": self.user_agent,
            "proxy": self.proxy
        }.items() if v is not None}

@dataclass
class RecaptchaV2Task(BaseTask):
    is_invisible: bool = False
    type: TaskType = field(default=TaskType.RECAPTCHA_V2, init=False)

    def to_dict(self) -> JsonDict:
        return {**super().to_dict(), "isInvisible": self.is_invisible}

@dataclass
class RecaptchaV3Task(BaseTask):
    min_score: Optional[float] = None
    page_action: Optional[str] = None
    type: TaskType = field(default=TaskType.RECAPTCHA_V3, init=False)

    def to_dict(self) -> JsonDict:
        return {**super().to_dict(), **{k: v for k, v in {
            "minScore": self.min_score,
            "pageAction": self.page_action
        }.items() if v is not None}}

@dataclass
class HCaptchaTask(BaseTask):
    invisible: bool = False
    enterprise: bool = False
    type: TaskType = field(default=TaskType.HCAPTCHA, init=False)

    def to_dict(self) -> JsonDict:
        return {**super().to_dict(), **{
            "invisible": self.invisible,
            "enterprise": self.enterprise
        }}

@dataclass
class TurnstileTask(BaseTask):
    type: TaskType = field(default=TaskType.TURNSTILE, init=False)

@dataclass
class FunCaptchaTask(BaseTask):
    type: TaskType = field(default=TaskType.FUNCAPTCHA, init=False)
