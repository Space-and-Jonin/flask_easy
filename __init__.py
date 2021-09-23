from .result import Result as Result
from .notification_handler import NotificationHandler as NotificationHandler
from .notifier import Notifier as Notifier
from .utils import auth_role as auth_role
from .utils import validator as validator
from .service_result import handle_result as handle_result
from .exceptions import AppException as AppException
from .instance import FlaskEasy as FlaskEasy

__all__ = [
    "Result",
    "auth_role",
    "validator",
    "handle_result",
    "AppException",
    "FlaskEasy",
    "Notifier",
    "NotificationHandler",
]
__version__ = "0.1.0"
