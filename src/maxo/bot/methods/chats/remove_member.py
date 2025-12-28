from retejo.http.markers import QueryParam, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.simple_query_result import SimpleQueryResult


class RemoveMember(MaxoMethod[SimpleQueryResult]):
    """Удаление участника из группового чата."""

    __url__ = "chats/{chat_id}/members"
    __http_method__ = "delete"

    chat_id: UrlVar[int]

    user_id: QueryParam[int]
    block: QueryParam[Omittable[bool]] = Omitted()
