from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class DeleteChat(MaxoMethod[SimpleQueryResult]):
    """Удаление группового чата."""

    __url__ = "chats/{chat_id}"
    __http_method__ = "delete"

    chat_id: UrlVar[int]
