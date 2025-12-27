from decimal import Decimal

from maxo.enums.attachment_request_type import AttachmentRequestType
from maxo.types.attachment_request import AttachmentRequest


class LocationAttachmentRequest(AttachmentRequest):
    """
    Запрос на прикрепление клавиатуры к сообщению.
    Запрос на прикрепление локации.

    Args:
        latitude: Ширина
        longitude: Долгота

    """

    type: AttachmentRequestType = AttachmentRequestType.LOCATION

    latitude: Decimal
    longitude: Decimal
