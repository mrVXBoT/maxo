from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.chat_member import ChatMember


class GetMembership(MaxoMethod[ChatMember]):
    """Получение информации о членстве бота в групповом чате."""

    __url__ = "chats/{chat_id}/members/me"
    __http_method__ = "get"

    chat_id: UrlVar[int]
