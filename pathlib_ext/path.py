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

    def prefix_stem(self, stem: str) -> "Path":
        """Return a new path with the prefix of stem changed"""
        new_stem = stem + self.stem
        return self.with_stem(new_stem)

    def postfix_stem(self, stem: str) -> "Path":
        """Return a new path with the postfix of stem changed"""
        new_stem = self.stem + stem
        return self.with_stem(new_stem)


class PosixPath(Path, pathlib.PurePosixPath):
    __slots__ = ()


class WindowsPath(Path, pathlib.PureWindowsPath):
    __slots__ = ()

    def is_mount(self):
        raise NotImplementedError("Path.is_mount() is unsupported on this system")
