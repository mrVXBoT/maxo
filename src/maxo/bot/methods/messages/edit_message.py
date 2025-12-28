from retejo.http.markers import Body, QueryParam

from maxo.bot.methods.base import MaxoMethod
from maxo.enums.text_format import TextFormat
from maxo.omit import Omittable, Omitted
from maxo.types.attachment_request import AttachmentRequest
from maxo.types.new_message_link import NewMessageLink
from maxo.types.simple_query_result import SimpleQueryResult


class EditMessage(MaxoMethod[SimpleQueryResult]):
    """Редактировать сообщение."""

    __url__ = "messages"
    __http_method__ = "put"

    message_id: QueryParam[str]

    attachments: Body[list[AttachmentRequest] | None] = None
    link: Body[NewMessageLink | None] = None
    text: Body[str | None] = None
    format: Body[Omittable[TextFormat | None]] = Omitted()
    notify: Body[Omittable[bool]] = Omitted()
