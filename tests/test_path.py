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


@pytest.mark.parametrize(
    "path,stem_prefix,result",
    (
        (Path("a/b"), "", Path("a/b")),
        (Path("a/b"), "d", Path("a/db")),
        (Path("/a/b"), "d", Path("/a/db")),
        (Path("a/b.py"), "d", Path("a/db.py")),
        (Path("/a/b.py"), "d", Path("/a/db.py")),
        (Path("/a/b.tar.gz"), "d", Path("/a/db.tar.gz")),
        (Path("a/Dot ending."), "d", Path("a/dDot ending.")),
        (Path("/a/Dot ending."), "d", Path("/a/dDot ending.")),
    ),
)
def test_prefix_stem_common(path, stem_prefix, result):
    assert path.prefix_stem(stem_prefix) == result


@pytest.mark.parametrize(
    "path,stem_prefix",
    (
        (Path(""), "d"),
        (Path("."), "d"),
        (Path("/"), "d"),
        (Path("a/b"), "/c"),
        (Path("a/b"), "c/"),
        (Path("a/b"), "c/d"),
    ),
)
def test_prefix_stem_raise_error(path, stem_prefix):
    with pytest.raises(ValueError):
        path.prefix_stem(stem_prefix)


@pytest.mark.parametrize(
    "path,stem_postfix,result",
    (
        (Path("a/b"), "", Path("a/b")),
        (Path("a/b"), "d", Path("a/bd")),
        (Path("/a/b"), "d", Path("/a/bd")),
        (Path("a/b.py"), "d", Path("a/bd.py")),
        (Path("/a/b.py"), "d", Path("/a/bd.py")),
        (Path("/a/b.tar.gz"), "d", Path("/a/b.tard.gz")),
        (Path("a/Dot ending."), "d", Path("a/Dot ending.d")),
        (Path("/a/Dot ending."), "d", Path("/a/Dot ending.d")),
    ),
)
def test_postfix_stem_common(path, stem_postfix, result):
    assert path.postfix_stem(stem_postfix) == result


@pytest.mark.parametrize(
    "path,stem_postfix",
    (
        (Path(""), "d"),
        (Path("."), "d"),
        (Path("/"), "d"),
        (Path("a/b"), "/c"),
        (Path("a/b"), "c/"),
        (Path("a/b"), "c/d"),
    ),
)
def test_postfix_stem_raise_error(path, stem_postfix):
    with pytest.raises(ValueError):
        path.postfix_stem(stem_postfix)
