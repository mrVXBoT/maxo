from enum import StrEnum


class Intent(StrEnum):
    """Намерение кнопки."""

    POSITIVE = "positive"
    NEGATIVE = "negative"
    DEFAULT = "default"
