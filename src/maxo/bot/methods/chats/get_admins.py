from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.chat_members_list import ChatMembersList


class GetAdmins(MaxoMethod[ChatMembersList]):
    """
    Получение списка администраторов группового чата.
    Результат получения списка администраторов чата.

    Args:
        chat_id: ID чата.

    """

    __url__ = "chats/{chat_id}/members/admins"
    __http_method__ = "get"

    chat_id: UrlVar[int]
