from maxo.types.attachment_payload import AttachmentPayload


class StickerAttachmentPayload(AttachmentPayload):
    """
    Содержимое вложения стикера.

    Args:
        url: URL медиа-вложения. Для видео-вложения используйте метод `GetVideoAttachmentDetails`, чтобы получить прямые ссылки.
        code: ID стикера.

    """

    code: str
