from typing import Self

from maxo.enums.attachment_type import AttachmentType
from maxo.types.attachment import Attachment
from maxo.types.sticker_attachment_payload import StickerAttachmentPayload


class StickerAttachment(Attachment):
    """
    Вложение стикера.

    Args:
        payload: Данные вложения стикера.
        width: Ширина стикера.
        height: Высота стикера.

    """

    type: AttachmentType = AttachmentType.STICKER

    payload: StickerAttachmentPayload
    width: int
    height: int

    @classmethod
    def factory(
        cls,
        url: str,
        code: str,
        width: int,
        height: int,
    ) -> Self:
        """
        Фабричный метод.

        Args:
            url: URL медиа-вложения. Для видео-вложения используйте метод `GetVideoAttachmentDetails`, чтобы получить прямые ссылки.
            code: ID стикера.
            width: Ширина стикера.
            height: Высота стикера.

        """
        return cls(
            payload=StickerAttachmentPayload(
                url=url,
                code=code,
            ),
            width=width,
            height=height,
        )
