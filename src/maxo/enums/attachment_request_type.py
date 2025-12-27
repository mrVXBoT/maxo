from enum import StrEnum


class AttachmentRequestType(StrEnum):
    """Запрос на прикрепление данных к сообщению."""

    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    STICKER = "sticker"
    CONTACT = "contact"
    INLINE_KEYBOARD = "inline_keyboard"
    LOCATION = "location"
    SHARE = "share"
