#!/usr/bin/python3
"""
This module consists of all the possible
test conditions for the method d0_create
"""
from console import HBNBCommand
from models.state import State
from models import storage
from io import StringIO
from sys import argv
from unittest.mock import patch
import unittest
import pycodestyle
import json
global id_t
global dic_tt


class TestConsole(unittest.TestCase):

    def test_create_method(self):
        """make sure a unique id is returned"""
        new_instance = State()
        new_instance.save()
        with patch('sys.stdout', new=StringIO()) as out:
            print(new_instance.id, end="")
            self.assertEqual(out.getvalue(), new_instance.id)

    def test_do_create_method(self):
        """make sure value is set while a unique id returned"""
        cns = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as out:
            cns.do_create('State name="California"')
            id_t = out.getvalue()
            self.assertEqual(out.getvalue(), id_t)
    
        # Make sure State name is set
        with open('file.json', encoding='utf-8') as f:
            content = f.read()
        id_tt = 'State.' + id_t.replace('\n', '')
        dic_t = json.loads(content)
        dic_tt = dic_t[id_tt]
        self.assertEqual(dic_tt['name'], 'California')

    def test_do_create_method_2(self):
        """make sure value is set while a unique id returned"""
        cns = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as out:
            cns.do_create('State name="Arizona"')
            id_t = out.getvalue()
            self.assertEqual(out.getvalue(), id_t)
    
        # make sure State name is Arizona
        with open('file.json', encoding='utf-8') as f:
            content = f.read()
        id_tt = 'State.' + id_t.replace('\n', '')
        dic_t = json.loads(content)
        dic_tt = dic_t[id_tt]
        self.assertEqual(dic_tt['name'], 'Arizona')

    def test_do_create_method_3(self):
        """Test do_create method """
        global id_t
        cns = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as out:
            cns.do_create('Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            id_t = out.getvalue()
            self.assertEqual(out.getvalue(), id_t)

    def test_do_create_method_4(self):
        """make sure all keys are set """
        global dic_tt
        with open('file.json', encoding='utf-8') as f:
            content = f.read()
        id_tt = 'Place.' + id_t.replace('\n', '')
        dic_t = json.loads(content)
        key_list = dic_t[id_tt].keys()
        dic_tt = dic_t[id_tt]

        self.assertIn('city_id', key_list)
        self.assertIn('user_id', key_list)
        self.assertIn('name', key_list)
        self.assertIn('number_rooms', key_list)
        self.assertIn('number_bathrooms', key_list)
        self.assertIn('max_guest', key_list)
        self.assertIn('price_by_night', key_list)
        self.assertIn('latitude', key_list)
        self.assertIn('longitude', key_list)
    
    def test_do_create_method_5(self):
        """make sure all values are as intended """
        
        self.assertEqual(dic_tt['city_id'], '0001')
        self.assertEqual(dic_tt['user_id'], '0001')
        self.assertEqual(dic_tt['name'], 'My little house')
        self.assertEqual(dic_tt['number_rooms'], 4)
        self.assertEqual(dic_tt['number_bathrooms'], 2)
        self.assertEqual(dic_tt['max_guest'], 10)
        self.assertEqual(dic_tt['price_by_night'], 300)
        self.assertEqual(dic_tt['latitude'], 37.773972)
        self.assertEqual(dic_tt['longitude'], -122.431297)

    def test_pycodestyle(self):
        """Check PEP 8 style """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")
