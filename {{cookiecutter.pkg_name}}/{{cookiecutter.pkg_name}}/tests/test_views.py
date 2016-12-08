"""Tests for views."""
from pyramid import testing
from unittest import TestCase
from unittest import mock


class TestViews(TestCase):

    def setUp(self):
        self.request = testing.DummyRequest()

    def tearDown(self):
        pass

    def test_home(self):
        from {{cookiecutter.pkg_name}}.views import home

        res = home(self.request)
        self.assertEqual(res["project"], "{{cookiecutter.pkg_name}}")
