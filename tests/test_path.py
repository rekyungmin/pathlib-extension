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
def test_prepend_stem_common(path, stem_prefix, result):
    assert path.prepend_stem(stem_prefix) == result


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
def test_prepend_stem_raise_error(path, stem_prefix):
    with pytest.raises(ValueError):
        path.prepend_stem(stem_prefix)


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
def test_append_stem_common(path, stem_postfix, result):
    assert path.append_stem(stem_postfix) == result


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
def test_append_stem_raise_error(path, stem_postfix):
    with pytest.raises(ValueError):
        path.append_stem(stem_postfix)


@pytest.mark.parametrize(
    "path,parent,result",
    (
        (Path("a/b"), "d", Path("d/b")),
        (Path("/a/b"), "d", Path("/d/b")),
        (Path("a/b.py"), "d", Path("d/b.py")),
        (Path("/a/b.py"), "d", Path("/d/b.py")),
        (Path("a/b"), "", Path("b")),
        (Path("a/b/c/d/e"), "/z", Path("/z/e")),
    ),
)
def test_with_parent_common(path, parent, result):
    assert path.with_parent(parent) == result


@pytest.mark.parametrize(
    "path,parent",
    (
        (Path(""), "d"),
        (Path("."), "d"),
        (Path("/"), "d"),
        (Path("a"), "d"),
        (Path("/a"), "d"),
        (Path("a/"), "d"),
    ),
)
def test_with_parent_raise_error(path, parent):
    with pytest.raises(ValueError):
        path.with_parent(parent)


@pytest.mark.parametrize(
    "path,new_suffix,result",
    (
        (Path("b.txt"), ".zip", Path("b.txt.zip")),
        (Path("/b.txt"), ".zip", Path("/b.txt.zip")),
        (Path("a/b.tar"), ".gz", Path("a/b.tar.gz")),
        (Path("/a/b.tar"), ".gz", Path("/a/b.tar.gz")),
        (Path("a/b.tar"), "", Path("a/b.tar")),
        (Path("/a/b"), "", Path("/a/b")),
    ),
)
def test_push_suffix_common(path, new_suffix, result):
    assert path.push_suffix(new_suffix) == result


@pytest.mark.parametrize(
    "path,new_suffix",
    (
        (Path(""), ".gz"),
        (Path("."), ".gz"),
        (Path("/"), ".gz"),
        (Path("a/b"), "zip"),
        (Path("a/b"), "/"),
        (Path("a/b"), "."),
        (Path("a/b"), "/.gz"),
        (Path("a/b"), ".c/.d"),
        (Path("a/b"), "./.d"),
        (Path("a/b"), "./.d"),
        (Path("a/b"), ".d/."),
        (Path("a/b.gz"), "zip"),
        (Path("a/b.gz"), "/"),
        (Path("a/b.gz"), "."),
        (Path("a/b.gz"), "/.gz"),
        (Path("a/b.gz"), ".c/.d"),
        (Path("a/b.gz"), "./.d"),
        (Path("a/b.gz"), "./.d"),
        (Path("a/b.gz"), ".d/."),
    ),
)
def test_push_suffix_raise_error(path, new_suffix):
    with pytest.raises(ValueError):
        path.push_suffix(new_suffix)


@pytest.mark.parametrize(
    "path,result",
    (
        (Path("b.txt"), Path("b")),
        (Path("/b.txt"), Path("/b")),
        (Path("b."), Path("b.")),
        (Path("b"), Path("b")),
    ),
)
def test_pop_suffix_common(path, result):
    assert path.pop_suffix() == result
