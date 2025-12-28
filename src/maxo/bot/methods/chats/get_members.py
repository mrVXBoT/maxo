from retejo.http.markers import QueryParam, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.chat_members_list import ChatMembersList


class GetMembers(MaxoMethod[ChatMembersList]):
    """Получение участников группового чата."""

    __url__ = "chats/{chat_id}/members"
    __http_method__ = "get"

    chat_id: UrlVar[int]

    count: QueryParam[Omittable[int]] = Omitted()
    marker: QueryParam[Omittable[int]] = Omitted()
    user_ids: QueryParam[Omittable[list[int] | None]] = Omitted()
