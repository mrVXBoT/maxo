from datetime import datetime

from maxo.omit import Omittable, Omitted
from maxo.types.base import MaxoType


class User(MaxoType):
    """
    Объект, описывающий пользователя. Имеет несколько вариаций (наследований):  - [`User`](/docs-api/objects/User) - [`UserWithPhoto`](/docs-api/objects/UserWithPhoto) - [`BotInfo`](/docs-api/objects/BotInfo) - [`ChatMember`](/docs-api/objects/ChatMember).
    Информация о пользователе.

    Args:
        user_id: ID пользователя.
        first_name: Отображаемое имя пользователя.
        last_name: Отображаемая фамилия пользователя.
        username:
            Уникальное публичное имя пользователя.
            Может быть null, если пользователь недоступен или имя не задано.
        is_bot: True, если пользователь является ботом.
        last_activity_time:
            Время последней активности пользователя в MAX (Unix-время в миллисекундах).
            Может быть неактуальным, если пользователь отключил статус "онлайн" в настройках.
        description:
            Описание пользователя.
            Может быть null, если пользователь его не заполнил.
            До 16000 символов.

    """

    user_id: int
    first_name: str
    last_name: str | None = None
    name: Omittable[str | None] = Omitted()
    username: str | None = None
    is_bot: bool
    last_activity_time: datetime

    @property
    def id(self) -> int:
        return self.user_id

    @property
    def fullname(self) -> str | None:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        return None
