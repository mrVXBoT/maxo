from maxo.omit import Omittable, Omitted
from maxo.types.base import MaxoType
from maxo.types.photo_attachment_payload import PhotoAttachmentPayload
from maxo.types.video_urls import VideoUrls


class VideoAttachmentDetails(MaxoType):
    token: str
    urls: Omittable[VideoUrls | None] = Omitted()
    thumbnail: Omittable[PhotoAttachmentPayload | None] = Omitted()
    width: int
    height: int
    duration: int
