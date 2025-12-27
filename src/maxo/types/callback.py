from datetime import datetime

from maxo.omit import Omittable, Omitted
from maxo.types.base import MaxoType
from maxo.types.user import User


class Callback(MaxoType):
    """Объект, отправленный боту, когда пользователь нажимает кнопку."""

    timestamp: datetime
    callback_id: str
    payload: Omittable[str] = Omitted()
    user: User

    @property
    def id(self) -> str:
        return self.callback_id
