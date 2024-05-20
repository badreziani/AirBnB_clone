#!/usr/bin/python3
"""
test_console module - contains tests for the HBNBCommand class
"""

import unittest
from unittest.mock import patch
from io import StringIO
import uuid
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for all feautures of the Console"""

    def setUp(self):
        """Setup method"""

        pass

    def tearDown(self):
        """Tear down method"""

        # tear down file.json
        pass

    def test_quit(self):
        """Test quit command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_EOF(self):
        """Test EOF command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "\n")

    def test_help(self):
        """Test help command"""
        
        output = "Prints the string representation of an instance\n"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), output)

    def test_emptyline(self):
        """Test emptyline command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual(f.getvalue(), "")

    def test_create(self):
        """Test create command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertEqual(len(f.getvalue().strip("\n")), 36)

    def test_show(self):
        """Test show command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Base")
            self.assertEqual(f.getvalue().strip("\n"), "** class doesn't exist **")

    def test_destroy(self):
        """Test destroy command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertEqual(f.getvalue().strip("\n"), "** instance id missing **")

    def test_all(self):
        """Test all command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue("BaseModel" in f.getvalue())

    def test_update(self):
        """Test update command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
            self.assertEqual(f.getvalue().strip("\n"), "** instance id missing **")
    
    def test_dot_all(self):
        """Test class.all() command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            self.assertTrue("BaseModel" in f.getvalue())

    '''
    def test_count(self):
        """Test count command"""

        with patch('sys.stdout', new=StringIO()) as f:
            string = "BaseModel.count()"
            HBNBCommand().onecmd(string.strip("\n"))
            self.assertTrue(type(int(f.getvalue()) == int))
    '''
