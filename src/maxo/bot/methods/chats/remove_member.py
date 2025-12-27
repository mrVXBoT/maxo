from retejo.http.markers import QueryParam, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.simple_query_result import SimpleQueryResult


class RemoveMember(MaxoMethod[SimpleQueryResult]):
    """
    Удаление участника из чата.

    Удаляет участника из чата. Для этого могут потребоваться дополнительные права.

    Источник: https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/members

    Args:
        chat_id: ID чата.
        user_id: ID пользователя, которого нужно удалить из чата.
        block:
            Если установлено в true, пользователь будет заблокирован в чате.
            Применяется только для чатов с публичной или приватной ссылкой.
            Игнорируется в остальных случаях.

    """

    __url__ = "chats/{chat_id}/members"
    __http_method__ = "delete"

    chat_id: UrlVar[int]

    user_id: QueryParam[int]
    block: QueryParam[Omittable[bool]] = Omitted()
