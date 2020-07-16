from golinks.models import GoRecord

test_record = GoRecord("name", "http://domain.com/{optional/^}")


def test_name():
    assert test_record.name == "name"


def test_url():
    assert test_record.url == "http://domain.com/{optional/^}"


def test_repr():
    assert repr(test_record) == "<GoRecord name>"


def test_favicon():
    assert test_record.favicon == "http://domain.com/favicon.ico"


def test_urlplain():
    assert test_record.url_plain == 'http://domain.com/'


def test_link_without_optional():
    assert test_record.link() == 'http://domain.com/'


def test_link_with_optional():
    assert test_record.link('my') == 'http://domain.com/optional/my'


def test_bad_optional():
    local_test = GoRecord('name', 'http://domain.com/{')
    assert local_test.link('my') == 'http://domain.com/{'
