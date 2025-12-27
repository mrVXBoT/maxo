from maxo.types.attachment import Attachment
from maxo.types.buttons import ReplyButtons


class ReplyKeyboardAttachment(Attachment):
    """Custom reply keyboard in message."""

    buttons: list[list[ReplyButtons]]
