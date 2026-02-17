from collections.abc import Callable, Sequence
from operator import itemgetter
from typing import TYPE_CHECKING, Any

from maxo.dialogs.tools.dialog_filter import DialogFilter, is_dialog_filter

if TYPE_CHECKING:
    from maxo.dialogs.integrations.magic_filter import MagicDialogFilter


# Try to import magic_filter
try:
    from magic_filter import MagicFilter as _MagicFilter
    _HAS_MAGIC_FILTER = True
except ImportError:  # pragma: no cover
    _HAS_MAGIC_FILTER = False
    _MagicFilter = None  # type: ignore[misc, assignment]


ItemsGetter = Callable[[dict], Sequence]
ItemsGetterVariant = str | ItemsGetter | DialogFilter | Sequence


def _get_identity(items: Sequence) -> ItemsGetter:
    def identity(data: Any) -> Sequence:
        return items

    return identity


def _get_dialog_filter_getter(f: DialogFilter) -> ItemsGetter:
    def items_filter(data: dict) -> Sequence:
        items = f.resolve(data)
        if isinstance(items, Sequence):
            return items
        return []

    return items_filter


def get_items_getter(attr_val: ItemsGetterVariant) -> ItemsGetter:
    if isinstance(attr_val, str):
        return itemgetter(attr_val)
    elif is_dialog_filter(attr_val):
        return _get_dialog_filter_getter(attr_val)
    elif _HAS_MAGIC_FILTER and isinstance(attr_val, _MagicFilter):
        # Handle magic_filter.MagicFilter if available
        from maxo.dialogs.integrations.magic_filter import MagicDialogFilter
        return _get_dialog_filter_getter(MagicDialogFilter(attr_val))
    elif callable(attr_val):
        return attr_val
    return _get_identity(attr_val)
