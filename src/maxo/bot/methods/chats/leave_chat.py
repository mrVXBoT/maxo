from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class LeaveChat(MaxoMethod[SimpleQueryResult]):
    """
    Удаление бота из чата.

    Удаляет бота из участников чата.

    Источник: https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members/me

    Args:
        chat_id: ID чата.

    """

    __url__ = "chats/{chat_id}/members/me"
    __http_method__ = "delete"

    chat_id: UrlVar[int]
