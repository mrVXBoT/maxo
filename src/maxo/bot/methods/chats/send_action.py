from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.enums.sender_action import SenderAction
from maxo.types.simple_query_result import SimpleQueryResult


class SendAction(MaxoMethod[SimpleQueryResult]):
    """
    Отправка действия в чат.

    Позволяет отправлять действия бота в чат,
    такие как «набор текста» или «отправка фото».

    Источник: https://dev.max.ru/docs-api/methods/POST/chats/-chatId-/actions

    Args:
        chat_id: ID чата.
        action: Действие, отправляемое участникам чата.

    """

    __url__ = "chats/{chat_id}/actions"
    __http_method__ = "post"

    chat_id: UrlVar[int]
    action: Body[SenderAction]
