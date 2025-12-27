from maxo.enums import AttachmentRequestType
from maxo.types.base import MaxoType


class AttachmentRequest(MaxoType):
    """Запрос на прикрепление данных к сообщению."""

    type: AttachmentRequestType
