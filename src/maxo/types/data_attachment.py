from maxo.enums.attachment_type import AttachmentType
from maxo.types.attachment import Attachment


class DataAttachment(Attachment):
    """
    Attachment contains payload sent through `SendMessageButton`

    Args:
        data:
        type:

    """

    type: AttachmentType = AttachmentType.DATA

    data: str
