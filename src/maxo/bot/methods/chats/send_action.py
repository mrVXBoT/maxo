from retejo.http.markers import Body, UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.enums.sender_action import SenderAction
from maxo.types.simple_query_result import SimpleQueryResult


class SendAction(MaxoMethod[SimpleQueryResult]):
    """Отправка действия бота в групповой чат."""

    __url__ = "chats/{chat_id}/actions"
    __http_method__ = "post"

    chat_id: UrlVar[int]

    action: Body[SenderAction]
