from typing import TYPE_CHECKING, Any, final

try:
    from magic_filter import AttrDict, MagicFilter as _MagicFilter
except ImportError as e:  # pragma: no cover
    e.add_note(" * Please run `pip install maxo[magic_filter]`")
    raise

if TYPE_CHECKING:
    from maxo.dialogs.tools.dialog_filter import DialogFilter


@final
class MagicDialogFilter:
    """
    Adapter that wraps magic_filter.MagicFilter to implement DialogFilter protocol.
    """

    __slots__ = ("_magic_filter",)

    def __init__(self, magic_filter: _MagicFilter) -> None:
        self._magic_filter = magic_filter

    def resolve(self, data: dict[str, Any]) -> Any:
        """Resolve the magic filter against the provided data."""
        return self._magic_filter.resolve(AttrDict(data))

    @classmethod
    def is_magic_filter(cls, obj: Any) -> bool:
        """Check if an object is a magic_filter.MagicFilter instance."""
        return isinstance(obj, _MagicFilter)

    @classmethod
    def wrap_if_needed(cls, obj: Any) -> "DialogFilter | Any":
        """
        Wrap a magic_filter.MagicFilter in MagicDialogFilter if needed.

        :param obj: Object to potentially wrap
        :return: Wrapped MagicDialogFilter if obj is MagicFilter, otherwise obj
        """
        if isinstance(obj, _MagicFilter):
            return cls(obj)
        return obj
