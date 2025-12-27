from retejo.http.markers import QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.omit import Omittable, Omitted
from maxo.types.send_message_result import SendMessageResult


class SendMessage(MaxoMethod[SendMessageResult]):
    """Отправить сообщение."""

    __url__ = "messages"
    __http_method__ = "post"

    user_id: QueryParam[Omittable[int]] = Omitted()
    chat_id: QueryParam[Omittable[int]] = Omitted()
    disable_link_preview: QueryParam[Omittable[bool]] = Omitted()
