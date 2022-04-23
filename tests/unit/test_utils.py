# -*- coding: utf-8 -*-
import re
import pytest
import django_sites as sites

from users.utils import get_absolute_url, is_absolute_url, build_url, \
    validate_private_url, IpAddresValueError, HostnameException

pytestmark = pytest.mark.django_db(transaction=True)


def test_is_absolute_url():
    assert is_absolute_url("http://domain/path")
    assert is_absolute_url("https://domain/path")
    assert not is_absolute_url("://domain/path")


def test_get_absolute_url():
    site = sites.get_current()
    assert get_absolute_url("http://domain/path") == "http://domain/path"
    assert get_absolute_url("/path") == build_url("/path", domain=site.domain, scheme=site.scheme)

@pytest.mark.parametrize("url", [
    "http://127.0.0.1",
    "http://[::1]",
    "http://192.168.0.12",
    "http://10.0.0.1",
    "https://172.25.0.1",
    "https://10.25.23.100",
    "ftp://192.168.1.100/",
    "http://[::ffff:c0a8:164]/",
    "scp://192.168.1.100/",
    "http://www.192-168-1-100.sslip.io/",
])
def test_validate_bad_destination_address(url):
    with pytest.raises(IpAddresValueError):
        validate_private_url(url)


@pytest.mark.parametrize("url", [
    "http://test.local/",
    "http://test.test/",
])
def test_validate_invalid_destination_address(url):
    with pytest.raises(HostnameException):
        validate_private_url(url)


@pytest.mark.parametrize("url", [
    "http://192.167.0.12",
    "http://11.0.0.1",
    "https://173.25.0.1",
    "https://193.24.23.100",
    "ftp://173.168.1.100/",
    "scp://194.168.1.100/",
    "http://www.google.com/",
    "http://1.1.1.1/",
])
def test_validate_good_destination_address(url):
    assert validate_private_url(url) is None