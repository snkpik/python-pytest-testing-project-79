import os  # noqa

import pytest
from page_loader import download



@pytest.fixture
def dir_for_tests(tmp_path):
    directory = tmp_path / "dir"
    directory.mkdir()
    return f"{tmp_path}/dir"


def test_page_loader_check_return_string(dir_for_tests, requests_mock):
    tmp_path = dir_for_tests

    requests_mock.get("https://ru.hexlet.io/courses", text="data")
    file_path = download("https://ru.hexlet.io/courses", tmp_path)

    assert file_path == f"{tmp_path}/ru-hexlet-io-courses.html"


def test_page_loader_check_requests_count(dir_for_tests, requests_mock):
    tmp_path = dir_for_tests

    requests_mock.get("https://some_page.com", text="data")
    download("https://some_page.com", tmp_path)

    assert requests_mock.call_count == 1
