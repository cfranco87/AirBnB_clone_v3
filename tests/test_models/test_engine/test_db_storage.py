#!/usr/bin/python3
"""
Contains the TestDBStorageDocs and TestDBStorage classes
"""

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
    def test_all_method(self):
        """Test the 'all' method of DBStorage."""
        # Add an instance of a class to the database
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

        # Test the 'all' method to check if the instance is present
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn(instance_id, output)

    def test_new_method(self):
        """Test the 'new' method of DBStorage."""
        # Add a new instance to the database using the 'new' method
        new_instance = BaseModel()
        models.storage.new(new_instance)
        models.storage.save()

        # Retrieve the instance from the database and check its existence
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"show BaseModel {new_instance.id}")
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(new_instance), output)

    def test_delete_method(self):
        """Test the 'delete' method of DBStorage."""
        # Add an instance to the database
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()

        # Delete the instance using the 'delete' method
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"destroy BaseModel {instance_id}")

        # Try to show the deleted instance and check if it's not found
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd(f"show BaseModel {instance_id}")
            output = mock_stdout.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""
    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_returns_dict(self):
        """Test that all returns a dictionaty"""
        self.assertIs(type(models.storage.all()), dict)

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(models.storage_t != 'db', "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
