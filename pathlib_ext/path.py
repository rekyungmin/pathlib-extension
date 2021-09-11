__all__ = (
    "PurePath",
    "PureWindowsPath",
    "PurePosixPath",
    "Path",
    "PosixPath",
    "WindowsPath",
)

import os
import pathlib
from typing import TypeVar

T = TypeVar("T", bound="PurePath")


class PurePath(pathlib.PurePath):
    __slots__ = ()

    def __new__(cls, *args):
        """Construct a PurePath from one or several strings and or existing
        PurePath objects.  The strings and path objects are combined so as
        to yield a canonicalized path, which is incorporated into the
        new PurePath object.
        """
        if cls is PurePath:
            cls = PureWindowsPath if os.name == "nt" else PurePosixPath
        return cls._from_parts(args)

    def with_stem(self: T, stem: str) -> T:
        """Return a new path with the stem changed."""
        return self.with_name(stem + self.suffix)

    def prepend_stem(self: T, stem: str) -> T:
        """Return a new path with the prefix of stem changed"""
        new_stem = stem + self.stem
        return self.with_stem(new_stem)

    def append_stem(self: T, stem: str) -> T:
        """Return a new path with the postfix of stem changed"""
        new_stem = self.stem + stem
        return self.with_stem(new_stem)

    def _count_changeable_node(self) -> int:
        if self.drive or self.root:
            return len(self.parts) - 1
        else:
            return len(self.parts)

    def with_parent(self: T, parent: str) -> T:
        """Return a new path with the parent changed"""
        if self._count_changeable_node() < 2:
            raise ValueError(f"{self} has an empty parent")

        parts = self.parts
        new_parts = [*parts[:-2], parent, parts[-1]]
        return self._from_parts(new_parts)  # type: ignore[attr-defined]

    def push_suffix(self: T, suffix: str) -> T:
        """Return a new path that pushed the new suffix with out removing the old one"""
        return self.with_suffix(suffix).append_stem(self.suffix)

    def pop_suffix(self: T) -> T:
        """Return a new path with the last suffix removed"""
        return self.with_suffix("")


class Path(PurePath):
    __slots__ = ()

    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == "nt" else PosixPath
        self = cls._from_parts(args, init=False)
        if not self._flavour.is_supported:
            raise NotImplementedError(
                "cannot instantiate %r on your system" % (cls.__name__,)
            )
        self._init()
        return self


class PosixPath(Path, pathlib.PurePosixPath):
    __slots__ = ()


class WindowsPath(Path, pathlib.PureWindowsPath):
    __slots__ = ()

    def is_mount(self):
        raise NotImplementedError("Path.is_mount() is unsupported on this system")


_windows_flavour = pathlib._WindowsFlavour()  # type: ignore[attr-defined]
_posix_flavour = pathlib._PosixFlavour()  # type: ignore[attr-defined]


class PureWindowsPath(PurePath):
    _flavour = _windows_flavour
    __slots__ = ()


class PurePosixPath(PurePath):
    _flavour = _posix_flavour
    __slots__ = ()
