from maxo.enums.attachment_request_type import AttachmentRequestType
from maxo.omit import Omittable, Omitted
from maxo.types.attachment_request import AttachmentRequest
from maxo.types.buttons import ReplyButtons


class ReplyKeyboardAttachmentRequest(AttachmentRequest):
    """
    Request to attach reply keyboard to message

    Args:
        buttons: Двумерный массив кнопок
        direct: Applicable only for chats. If `true` keyboard will be shown only for user bot mentioned or replied
        direct_user_id: If set to `true`, reply keyboard will only be shown to this participant in chat
        type:

    """

    type: AttachmentRequestType = AttachmentRequestType.REPLY_KEYBOARD

    buttons: list[list[ReplyButtons]]

    direct: Omittable[bool] = Omitted()
    direct_user_id: Omittable[int | None] = Omitted()
