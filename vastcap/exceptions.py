from typing import Optional

class VastCapException(Exception):
    def __init__(
      self, 
      message: str, 
      error_code: Optional[str] = None
    ) -> None:
        super().__init__(message)
        self.error_code = error_code

class InvalidAPIKeyError(VastCapException):
    pass

class InsufficientBalanceError(VastCapException):
    pass

class TaskNotFoundError(VastCapException):
    pass

class ValidationError(VastCapException):
    pass

class NoSlotAvailableError(VastCapException):
    pass

class IPBannedError(VastCapException):
    pass

class CaptchaUnsolvableError(VastCapException):
    pass

class ProxyConnectionError(VastCapException):
    pass

ERROR_MAPPING = {
    "ERROR_KEY_DOES_NOT_EXIST": InvalidAPIKeyError("Invalid API key"),
    "ERROR_INSUFFICIENT_BALANCE": InsufficientBalanceError("Insufficient balance"),
    "ERROR_VALIDATION_FAILED": ValidationError("Invalid request parameters"),
    "ERROR_NO_SLOT_AVAILABLE": NoSlotAvailableError("No available slots"),
    "ERROR_IP_BANNED": IPBannedError("Your IP address is banned"),
    "ERROR_TASK_NOT_FOUND": TaskNotFoundError("Task not found"),
    "ERROR_CAPTCHA_UNSOLVABLE": CaptchaUnsolvableError("Captcha unsolvable"),
    "ERROR_PROXY_CONNECTION_FAILED": ProxyConnectionError("Proxy connection failed")
}
