from retejo.http.markers import UrlVar

from maxo.bot.methods.base import MaxoMethod
from maxo.types.video_attachment_details import VideoAttachmentDetails


class GetVideoAttachmentDetails(MaxoMethod[VideoAttachmentDetails]):
    """Получить информацио о видео."""

    __url__ = "videos/{video_token}"
    __http_method__ = "get"

    video_token: UrlVar[str]
