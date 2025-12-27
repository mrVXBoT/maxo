from typing import Self

from maxo.enums.attachment_request_type import AttachmentRequestType
from maxo.omit import Omittable, Omitted
from maxo.types.attachment_request import AttachmentRequest
from maxo.types.upload_endpoint import UploadEndpoint


class VideoAttachmentRequest(AttachmentRequest):
    """
    Запрос на прикрепление видео к сообщению.
    Запрос на прикрепление изображения.

    Args:
        payload: Данные запроса на прикрепление изображения

    """

    type: AttachmentRequestType = AttachmentRequestType.VIDEO
    payload: UploadEndpoint

    @classmethod
    def factory(cls, token: Omittable[str] = Omitted()) -> Self:
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
