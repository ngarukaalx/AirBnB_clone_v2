#!/usr/bin/python3
""" module defines a class that tests Place """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ class that tests Place class """

    def __init__(self, *args, **kwargs):
        """ test init"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test id """
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_user_id(self):
        """  test user_id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_name(self):
        """ test name"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_description(self):
        """ test description """
        new = self.value()
        self.assertEqual(type(new.description), str if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_number_rooms(self):
        """ test number_rooms """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_number_bathrooms(self):
        """ test number_bathrooms """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_max_guest(self):
        """ test max_guest"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_price_by_night(self):
        """ test price_by_night """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_latitude(self):
        """ test latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_longitude(self):
        """ test longitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))

    def test_amenity_ids(self):
        """ test amenity_ids """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                         os.getenv('HBNB_TYPE_STORAGE') != 'db'
                         else type(None))
