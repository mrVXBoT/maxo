from datetime import datetime

from maxo.types.base import MaxoType


class Subscription(MaxoType):
    """Схема для описания подписки на WebHook."""

    url: str
    time: datetime
    update_types: list[str] | None = None
