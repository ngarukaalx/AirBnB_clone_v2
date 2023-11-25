#!/usr/bin/python3
""" module that tests reviews"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import os


class test_review(test_basemodel):
    """ class that tests Review """

    def __init__(self, *args, **kwargs):
        """ test init"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test place_id """
        new = self.value()
        self.assertEqual(type(new.place_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_user_id(self):
        """ test user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_text(self):
        """ test text """
        new = self.value()
        self.assertEqual(type(new.text), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))
