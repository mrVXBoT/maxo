from maxo.enums.attachment_type import AttachmentType
from maxo.types.attachment import Attachment


class LocationAttachment(Attachment):
    """
    Вложение локации.

    Args:
        latitude: Широта
        longitude: Долгота

    """

    type: AttachmentType = AttachmentType.LOCATION

    latitude: float
    longitude: float
