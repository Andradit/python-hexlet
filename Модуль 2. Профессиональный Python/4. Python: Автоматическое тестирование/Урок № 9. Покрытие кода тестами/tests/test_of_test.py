import os

import pytest

from test_plugin import TestPlugin


def run_tests():
    plugin = TestPlugin()
    pytest.main(["tests/test_solution.py"], plugins=[plugin])
    return plugin.passed_tests


def get_passed_tests_count():
    passed_tests = run_tests()
    print(passed_tests)
    return len(passed_tests)


def get_expected_count():
    return int(os.environ["PASSED_TESTS"])


def test_implementations():
    passed_tests = get_passed_tests_count()
    expected = get_expected_count()
    assert passed_tests == expected