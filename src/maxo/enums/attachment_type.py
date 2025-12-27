from enum import StrEnum


class AttachmentType(StrEnum):
    """Общая схема, представляющая вложение сообщения."""

    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    FILE = "file"
    STICKER = "sticker"
    CONTACT = "contact"
    INLINE_KEYBOARD = "inline_keyboard"
    SHARE = "share"
    LOCATION = "location"
