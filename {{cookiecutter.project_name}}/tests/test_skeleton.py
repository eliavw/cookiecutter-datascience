# -*- coding: utf-8 -*-

import pytest
from {{cookiecutter.project_name}}.skeleton import fib

__author__ = "{{cookiecutter.author_name}}"
__copyright__ = "{{cookiecutter.author_name}}"
__license__ = "{{cookiecutter.license}}"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
