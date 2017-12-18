from ds.urljoin import url_path_join


def test_url_path_join():
    assert url_path_join("http://example.com/", "/path/") == \
           "http://example.com/path"


def test_url_path_join_nested():
    assert url_path_join("http://example.com/", "/path/path") == \
           "http://example.com/path/path"


def test_url_path_join_single():
    assert url_path_join("http://example.com/") == \
           "http://example.com"


def test_url_path_join_trailing_slash():
    assert url_path_join("http://example.com/", "/path/",
                         trailing_slash=True) == \
           "http://example.com/path/"


def test_url_path_join_multiple():
    assert url_path_join("http://example.com/", "/path/", "a", "b") == \
           "http://example.com/path/a/b"
