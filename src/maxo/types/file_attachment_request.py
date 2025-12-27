from typing import Self

from maxo.enums.attachment_request_type import AttachmentRequestType
from maxo.types.attachment_request import AttachmentRequest
from maxo.types.upload_endpoint import UploadEndpoint


class FileAttachmentRequest(AttachmentRequest):
    """
    Запрос на прикрепление файла к сообщению.
    ДОЛЖЕН быть единственным вложением в сообщении.

    Args:
        payload: Данные запроса на прикрепление файла.

    """

    type: AttachmentRequestType = AttachmentRequestType.FILE
    payload: UploadEndpoint

    @classmethod
    def factory(cls, token: str) -> Self:
        """
        Фабричный метод.

        Args:
            token: Токен — уникальный ID загруженного медиафайла.

        """
        return cls(
            payload=UploadEndpoint(
                token=token,
            ),
        )
