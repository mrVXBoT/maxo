from enum import StrEnum


class ChatStatus(StrEnum):
    """Статус чата для текущего бота."""

    ACTIVE = "active"
    REMOVED = "removed"
    LEFT = "left"
    CLOSED = "closed"
