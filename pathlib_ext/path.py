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


class PosixPath(Path, pathlib.PurePosixPath):
    __slots__ = ()


class WindowsPath(Path, pathlib.PureWindowsPath):
    __slots__ = ()

    def is_mount(self):
        raise NotImplementedError("Path.is_mount() is unsupported on this system")
