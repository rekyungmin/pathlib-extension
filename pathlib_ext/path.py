__all__ = (
    "Path",
    "PosixPath",
    "WindowsPath",
)

import os
import pathlib


class Path(pathlib.Path):
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

    def with_stem(self, stem: str) -> "Path":
        """Return a new path with the stem changed."""
        return self.with_name(stem + self.suffix)

    def prepend_stem(self, stem: str) -> "Path":
        """Return a new path with the prefix of stem changed"""
        new_stem = stem + self.stem
        return self.with_stem(new_stem)

    def append_stem(self, stem: str) -> "Path":
        """Return a new path with the postfix of stem changed"""
        new_stem = self.stem + stem
        return self.with_stem(new_stem)

    def _count_changeable_node(self) -> int:
        if self.drive or self.root:
            return len(self.parts) - 1
        else:
            return len(self.parts)

    def with_parent(self, parent: str) -> "Path":
        """Return a new path with the parent changed"""
        if self._count_changeable_node() < 2:
            raise ValueError(f"{self} has an empty parent")

        new_parts = [*self.parts[:-2], parent, self.parts[-1]]
        return Path(*new_parts)


class PosixPath(Path, pathlib.PurePosixPath):
    __slots__ = ()


class WindowsPath(Path, pathlib.PureWindowsPath):
    __slots__ = ()

    def is_mount(self):
        raise NotImplementedError("Path.is_mount() is unsupported on this system")
