from .client import Vast, AsyncVast
from .types import (
    TaskType,
    TaskStatus,
    SolverError,
    TaskSolution,
    BaseTask,
    RecaptchaV2Task,
    RecaptchaV3Task,
    HCaptchaTask,
    TurnstileTask,
    FunCaptchaTask
)

__version__ = "1.0.0"
__all__ = [
    "Vast",
    "AsyncVast",
    "TaskType",
    "TaskStatus",
    "SolverError",
    "TaskSolution",
    "BaseTask",
    "RecaptchaV2Task",
    "RecaptchaV3Task",
    "HCaptchaTask",
    "TurnstileTask",
    "FunCaptchaTask",
]
