from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types import ChatAdmin
from maxo.types.simple_query_result import SimpleQueryResult


class SetAdmins(MaxoMethod[SimpleQueryResult]):
    """
    Назначить администраторов чата.

    Возвращает значение true, если добавлены все администраторы.

    Источник: https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members/admins

    Args:
        chat_id: ID чата.
        admins: Массив администраторов чата.

    """

    __url__ = "chats/{chat_id}/members/admins"
    __http_method__ = "post"

    chat_id: UrlVar[int]

    admins: Body[list[ChatAdmin]]
