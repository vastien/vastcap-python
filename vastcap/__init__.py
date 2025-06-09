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

from .exceptions import *

# I usually despise wildcard imports, but this is fine.

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
