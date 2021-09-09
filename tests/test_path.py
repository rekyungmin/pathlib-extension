import pytest

from pathlib_ext.path import Path


@pytest.mark.parametrize(
    "path,stem,result",
    (
        (Path("a/b"), "d", Path("a/d")),
        (Path("/a/b"), "d", Path("/a/d")),
        (Path("a/b.py"), "d", Path("a/d.py")),
        (Path("/a/b.py"), "d", Path("/a/d.py")),
        (Path("/a/b.tar.gz"), "d", Path("/a/d.gz")),
        (Path("a/Dot ending."), "d", Path("a/d")),
        (Path("/a/Dot ending."), "d", Path("/a/d")),
    ),
)
def test_with_stem_common(path, stem, result):
    assert path.with_stem(stem) == result


@pytest.mark.parametrize(
    "path,stem",
    (
        (Path(""), "d"),
        (Path("."), "d"),
        (Path("/"), "d"),
        (Path("a/b"), ""),
        (Path("a/b"), "/c"),
        (Path("a/b"), "c/"),
        (Path("a/b"), "c/d"),
    ),
)
def test_with_stem_raise_error(path, stem):
    with pytest.raises(ValueError):
        path.with_stem(stem)
