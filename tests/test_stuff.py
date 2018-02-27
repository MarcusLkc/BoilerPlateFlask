import unittest
from flask_testing import TestCase
from flask import current_app
from app import create_app, db


class BasicsTestCase(TestCase):
    def create_app(self):
        return create_app('config.TestingConfig')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_equal(self):
        self.assertTrue(5 == 5)

    def test_app_exists(self):
        self.assertFalse(current_app is None)
