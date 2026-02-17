from collections.abc import Callable
from typing import TYPE_CHECKING, Any

from maxo.dialogs.api.internal import RawKeyboard
from maxo.dialogs.api.protocols import DialogManager
from maxo.dialogs.tools.dialog_filter import DialogFilter, is_dialog_filter
from maxo.dialogs.widgets.common.scroll import (
    BaseScroll,
    OnPageChangedVariants,
)

if TYPE_CHECKING:
    from maxo.dialogs.integrations.magic_filter import MagicDialogFilter


# Try to import magic_filter
try:
    from magic_filter import MagicFilter as _MagicFilter
    _HAS_MAGIC_FILTER = True
except ImportError:  # pragma: no cover
    _HAS_MAGIC_FILTER = False
    _MagicFilter = None  # type: ignore[misc, assignment]

from .base import Keyboard

PagesGetter = Callable[[dict, "StubScroll", DialogManager], int]


def new_pages_field(fieldname: str) -> PagesGetter:
    def pages_field(
        data: dict,
        widget: "StubScroll",
        manager: DialogManager,
    ) -> int:
        return data.get(fieldname)

    return pages_field


def new_pages_dialog_filter(f: DialogFilter) -> PagesGetter:
    def pages_filter(
        data: dict,
        widget: "StubScroll",
        manager: DialogManager,
    ) -> int:
        return f.resolve(data)

    return pages_filter


def new_pages_fixed(pages: int) -> PagesGetter:
    def pages_fixed(
        data: dict,
        widget: "StubScroll",
        manager: DialogManager,
    ) -> int:
        return pages

    return pages_fixed


class StubScroll(Keyboard, BaseScroll):
    def __init__(
        self,
        id: str,
        pages: str | int | PagesGetter | DialogFilter,
        on_page_changed: OnPageChangedVariants = None,
    ) -> None:
        Keyboard.__init__(self, id=id, when=None)
        BaseScroll.__init__(self, id=id, on_page_changed=on_page_changed)
        if isinstance(pages, str):
            self._pages = new_pages_field(pages)
        elif isinstance(pages, int):
            self._pages = new_pages_fixed(pages)
        elif is_dialog_filter(pages):
            self._pages = new_pages_dialog_filter(pages)
        elif _HAS_MAGIC_FILTER and isinstance(pages, _MagicFilter):
            # Handle magic_filter.MagicFilter if available
            from maxo.dialogs.integrations.magic_filter import MagicDialogFilter
            self._pages = new_pages_dialog_filter(MagicDialogFilter(pages))
        else:
            self._pages = pages

    async def _render_keyboard(
        self,
        data: dict,
        manager: DialogManager,
    ) -> RawKeyboard:
        return [[]]

    async def get_page_count(self, data: dict, manager: DialogManager) -> int:
        return self._pages(data, self, manager)
