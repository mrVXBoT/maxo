from maxo.omit import Omittable, Omitted
from maxo.types.attachment_request import AttachmentRequest
from maxo.types.buttons import ReplyButtons


class ReplyKeyboardAttachmentRequest(AttachmentRequest):
    """Request to attach reply keyboard to message."""

    direct: Omittable[bool] = Omitted()
    direct_user_id: Omittable[int | None] = Omitted()
    buttons: list[list[ReplyButtons]]
