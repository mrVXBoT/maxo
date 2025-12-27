from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.get_pinned_message_result import GetPinnedMessageResult


class GetPinnedMessage(MaxoMethod[GetPinnedMessageResult]):
    """
    Получение закрепленного сообщения.

    Возвращает закрепленное сообщение в чате.

    Источник: https://dev.max.ru/docs-api/methods/GET/chats/-chatId-/pin

    Args:
        chat_id: ID чата.

    """

    __url__ = "chats/{chat_id}/pin"
    __http_method__ = "get"

    chat_id: UrlVar[int]
