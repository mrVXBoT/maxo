from abc import abstractmethod
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class DialogFilter(Protocol):
    """
    Protocol for filter objects that can resolve values from data dictionaries.
    Compatible with magic_filter.MagicFilter interface.
    """

    @abstractmethod
    def resolve(self, data: dict[str, Any]) -> Any:
        """
        Resolve the filter against the provided data dictionary.

        :param data: Dictionary containing data to filter against
        :return: The resolved value (typically a boolean for condition checks)
        """
        raise NotImplementedError


# Type alias for filter-like objects
DialogFilterType = DialogFilter | Any


def is_dialog_filter(obj: Any) -> bool:
    """Check if an object implements the DialogFilter protocol."""
    return isinstance(obj, DialogFilter)
