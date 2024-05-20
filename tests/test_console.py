#!/usr/bin/python3
"""
test_console module - contains tests for the HBNBCommand class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for all feautures of the Console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    '''
    def test_help(self):
        """Test the help method"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

        help_string = "Prints the string representation of an instance"

        self.assertTrue(f.getvalue(), help_string)
    '''

    def test_quit(self):
        """Test quit command"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual(f.getvalue(), "")
