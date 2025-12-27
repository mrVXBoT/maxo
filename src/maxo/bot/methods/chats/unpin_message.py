from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.simple_query_result import SimpleQueryResult


class UnpinMessage(MaxoMethod[SimpleQueryResult]):
    """
    Удаление закрепленного сообщения.

    Удаляет закрепленное сообщение в чате.

    Источник: https://dev.max.ru/docs-api/methods/DELETE/chats/-chatId-/pin

    Args:
        chat_id: ID чата, у которого нужно удалить закрепленное сообщение.

    """

    __url__ = "chats/{chat_id}/pin"
    __http_method__ = "delete"

    chat_id: UrlVar[int]
