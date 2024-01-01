#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""
import io
import console
import inspect
import pep8
import unittest
from unittest.mock import patch
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")

    def test_create_instance(self):
        """Test creating a new instance using the 'create' command."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output != "")

    def test_update_attribute(self):
        """Test updating an attribute using the 'update' command."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            HBNBCommand().onecmd(
                f"update BaseModel {instance_id} name 'New Name'")
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                HBNBCommand().onecmd(f"show BaseModel {instance_id}")
                output = mock_stdout.getvalue().strip()
                self.assertIn("'name': 'New Name'", output)

    def test_destroy_instance(self):
        """Test destroying an instance using the 'destroy' command."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            HBNBCommand().onecmd("create BaseModel")
            instance_id = mock_stdout.getvalue().strip()
            HBNBCommand().onecmd(f"destroy BaseModel {instance_id}")
            with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                HBNBCommand().onecmd(f"show BaseModel {instance_id}")
                output = mock_stdout.getvalue().strip()
                self.assertEqual(output, "** no instance found **")
