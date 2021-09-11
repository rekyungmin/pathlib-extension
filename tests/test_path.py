import pytest

from pathlib_ext.path import PurePath


@pytest.mark.parametrize(
    "path,stem,result",
    (
        (PurePath("a/b"), "d", PurePath("a/d")),
        (PurePath("/a/b"), "d", PurePath("/a/d")),
        (PurePath("a/b.py"), "d", PurePath("a/d.py")),
        (PurePath("/a/b.py"), "d", PurePath("/a/d.py")),
        (PurePath("/a/b.tar.gz"), "d", PurePath("/a/d.gz")),
        (PurePath("a/Dot ending."), "d", PurePath("a/d")),
        (PurePath("/a/Dot ending."), "d", PurePath("/a/d")),
    ),
)
def test_with_stem_common(path, stem, result):
    assert path.with_stem(stem) == result


@pytest.mark.parametrize(
    "path,stem",
    (
        (PurePath(""), "d"),
        (PurePath("."), "d"),
        (PurePath("/"), "d"),
        (PurePath("a/b"), ""),
        (PurePath("a/b"), "/c"),
        (PurePath("a/b"), "c/"),
        (PurePath("a/b"), "c/d"),
    ),
)
def test_with_stem_raise_error(path, stem):
    with pytest.raises(ValueError):
        path.with_stem(stem)


@pytest.mark.parametrize(
    "path,stem_prefix,result",
    (
        (PurePath("a/b"), "", PurePath("a/b")),
        (PurePath("a/b"), "d", PurePath("a/db")),
        (PurePath("/a/b"), "d", PurePath("/a/db")),
        (PurePath("a/b.py"), "d", PurePath("a/db.py")),
        (PurePath("/a/b.py"), "d", PurePath("/a/db.py")),
        (PurePath("/a/b.tar.gz"), "d", PurePath("/a/db.tar.gz")),
        (PurePath("a/Dot ending."), "d", PurePath("a/dDot ending.")),
        (PurePath("/a/Dot ending."), "d", PurePath("/a/dDot ending.")),
    ),
)
def test_prepend_stem_common(path, stem_prefix, result):
    assert path.prepend_stem(stem_prefix) == result


@pytest.mark.parametrize(
    "path,stem_prefix",
    (
        (PurePath(""), "d"),
        (PurePath("."), "d"),
        (PurePath("/"), "d"),
        (PurePath("a/b"), "/c"),
        (PurePath("a/b"), "c/"),
        (PurePath("a/b"), "c/d"),
    ),
)
def test_prepend_stem_raise_error(path, stem_prefix):
    with pytest.raises(ValueError):
        path.prepend_stem(stem_prefix)


@pytest.mark.parametrize(
    "path,stem_postfix,result",
    (
        (PurePath("a/b"), "", PurePath("a/b")),
        (PurePath("a/b"), "d", PurePath("a/bd")),
        (PurePath("/a/b"), "d", PurePath("/a/bd")),
        (PurePath("a/b.py"), "d", PurePath("a/bd.py")),
        (PurePath("/a/b.py"), "d", PurePath("/a/bd.py")),
        (PurePath("/a/b.tar.gz"), "d", PurePath("/a/b.tard.gz")),
        (PurePath("a/Dot ending."), "d", PurePath("a/Dot ending.d")),
        (PurePath("/a/Dot ending."), "d", PurePath("/a/Dot ending.d")),
    ),
)
def test_append_stem_common(path, stem_postfix, result):
    assert path.append_stem(stem_postfix) == result


@pytest.mark.parametrize(
    "path,stem_postfix",
    (
        (PurePath(""), "d"),
        (PurePath("."), "d"),
        (PurePath("/"), "d"),
        (PurePath("a/b"), "/c"),
        (PurePath("a/b"), "c/"),
        (PurePath("a/b"), "c/d"),
    ),
)
def test_append_stem_raise_error(path, stem_postfix):
    with pytest.raises(ValueError):
        path.append_stem(stem_postfix)


@pytest.mark.parametrize(
    "path,parent,result",
    (
        (PurePath("a/b"), "d", PurePath("d/b")),
        (PurePath("/a/b"), "d", PurePath("/d/b")),
        (PurePath("a/b.py"), "d", PurePath("d/b.py")),
        (PurePath("/a/b.py"), "d", PurePath("/d/b.py")),
        (PurePath("a/b"), "", PurePath("b")),
        (PurePath("a/b/c/d/e"), "/z", PurePath("/z/e")),
    ),
)
def test_with_parent_common(path, parent, result):
    assert path.with_parent(parent) == result


@pytest.mark.parametrize(
    "path,parent",
    (
        (PurePath(""), "d"),
        (PurePath("."), "d"),
        (PurePath("/"), "d"),
        (PurePath("a"), "d"),
        (PurePath("/a"), "d"),
        (PurePath("a/"), "d"),
    ),
)
def test_with_parent_raise_error(path, parent):
    with pytest.raises(ValueError):
        path.with_parent(parent)


@pytest.mark.parametrize(
    "path,parent,result",
    (
        (PurePath("a/b"), "d", PurePath("a/d/b")),
        (PurePath("/a/b"), "d", PurePath("/a/d/b")),
        (PurePath("a/b.py"), "d", PurePath("a/d/b.py")),
        (PurePath("/a/b.py"), "d", PurePath("/a/d/b.py")),
        (PurePath("a/b"), "", PurePath("a/b")),
        (PurePath("a/b/c/d/e"), "/z", PurePath("/z/e")),
    ),
)
def test_push_parent_common(path, parent, result):
    assert path.push_parent(parent) == result


@pytest.mark.parametrize(
    "path,result",
    (
        (PurePath("a/b"), PurePath("b")),
        (PurePath("/a/b"), PurePath("/b")),
        (PurePath("a/b.py"), PurePath("b.py")),
        (PurePath("/a/b.py"), PurePath("/b.py")),
        (PurePath("b.py"), PurePath("b.py")),
        (PurePath("/b.py"), PurePath("/b.py")),
    ),
)
def test_pop_parent_common(path, result):
    assert path.pop_parent() == result


@pytest.mark.parametrize(
    "path,new_suffix,result",
    (
        (PurePath("b.txt"), ".zip", PurePath("b.txt.zip")),
        (PurePath("/b.txt"), ".zip", PurePath("/b.txt.zip")),
        (PurePath("a/b.tar"), ".gz", PurePath("a/b.tar.gz")),
        (PurePath("/a/b.tar"), ".gz", PurePath("/a/b.tar.gz")),
        (PurePath("a/b.tar"), "", PurePath("a/b.tar")),
        (PurePath("/a/b"), "", PurePath("/a/b")),
    ),
)
def test_push_suffix_common(path, new_suffix, result):
    assert path.push_suffix(new_suffix) == result


@pytest.mark.parametrize(
    "path,new_suffix",
    (
        (PurePath(""), ".gz"),
        (PurePath("."), ".gz"),
        (PurePath("/"), ".gz"),
        (PurePath("a/b"), "zip"),
        (PurePath("a/b"), "/"),
        (PurePath("a/b"), "."),
        (PurePath("a/b"), "/.gz"),
        (PurePath("a/b"), ".c/.d"),
        (PurePath("a/b"), "./.d"),
        (PurePath("a/b"), "./.d"),
        (PurePath("a/b"), ".d/."),
        (PurePath("a/b.gz"), "zip"),
        (PurePath("a/b.gz"), "/"),
        (PurePath("a/b.gz"), "."),
        (PurePath("a/b.gz"), "/.gz"),
        (PurePath("a/b.gz"), ".c/.d"),
        (PurePath("a/b.gz"), "./.d"),
        (PurePath("a/b.gz"), "./.d"),
        (PurePath("a/b.gz"), ".d/."),
    ),
)
def test_push_suffix_raise_error(path, new_suffix):
    with pytest.raises(ValueError):
        path.push_suffix(new_suffix)


@pytest.mark.parametrize(
    "path,result",
    (
        (PurePath("b.txt"), PurePath("b")),
        (PurePath("/b.txt"), PurePath("/b")),
        (PurePath("b."), PurePath("b.")),
        (PurePath("b"), PurePath("b")),
    ),
)
def test_pop_suffix_common(path, result):
    assert path.pop_suffix() == result
