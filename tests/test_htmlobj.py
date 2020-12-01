from selenium import webdriver


def test_url_exits(create_htmlobj):
    assert create_htmlobj.url is not None


def test_driver_is_webdriver_object(create_htmlobj):
    assert type(create_htmlobj.driver) == webdriver.Firefox


def test_ufs_returns_a_list_if_self_ufs_is_valid(create_htmlobj):
    assert type(create_htmlobj.ufs) == list


def test_ufs_returns_27_ufs_if_self_ufs_is_valid(create_htmlobj):
    assert len(create_htmlobj.ufs) == 27
