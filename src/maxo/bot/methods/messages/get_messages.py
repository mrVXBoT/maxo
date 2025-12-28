from typing import Any

from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.message_list import MessageList


class GetMessages(MaxoMethod[MessageList]):
    """Получение сообщений."""

    __url__ = "messages"
    __http_method__ = "get"

    chat_id: QueryParam[Omittable[int]] = Omitted()
    count: QueryParam[Omittable[int]] = Omitted()
    from_: QueryParam[Omittable[int]] = Omitted()
    message_ids: QueryParam[Omittable[Any | None]] = Omitted()
    to: QueryParam[Omittable[int]] = Omitted()
