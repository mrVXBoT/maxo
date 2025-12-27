from maxo.types.attachment_payload import AttachmentPayload


class MediaAttachmentPayload(AttachmentPayload):
    """
    Содержимое мультимедийного вложения.

    Args:
        url: URL медиа-вложения. Для видео-вложения используйте метод GetVideoAttachmentDetails, чтобы получить прямые ссылки.
        token: Используйте token, если вы пытаетесь повторно использовать одно и то же вложение в другом сообщении.

    """

    token: str
