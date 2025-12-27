from maxo.omit import Omittable, Omitted
from maxo.types.user import User


class UserWithPhoto(User):
    """
    Объект пользователя с фотографией.
    Информация о пользователе c фото.

    Args:
        avatar_url: URL аватара
        full_avatar_url: URL аватара большего размера

    """

    description: Omittable[str | None] = Omitted()
    avatar_url: Omittable[str] = Omitted()
    full_avatar_url: Omittable[str] = Omitted()
