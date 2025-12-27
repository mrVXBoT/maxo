from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.chat_list import ChatList


class GetChats(MaxoMethod[ChatList]):
    """Получение списка всех групповых чатов."""

    __url__ = "chats"
    __http_method__ = "get"

    count: QueryParam[Omittable[int]] = Omitted()
    marker: QueryParam[Omittable[int]] = Omitted()
