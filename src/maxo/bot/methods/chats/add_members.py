from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class AddMembers(MaxoMethod[SimpleQueryResult]):
    """
    Добавление участников в чат.

    Добавляет участников в чат. Для этого могут потребоваться дополнительные права.

    Источник: https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/members

    Args:
        chat_id: ID чата.
        user_ids: Массив ID пользователей для добавления в чат.

    """

    __url__ = "chats/{chat_id}/members"
    __http_method__ = "post"

    chat_id: UrlVar[int]

    user_ids: Body[list[int]]
