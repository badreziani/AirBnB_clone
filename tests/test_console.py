#!/usr/bin/python3
"""
test_console module - contains tests for the HBNBCommand class
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
import sys


class TestHBNBCommand(unittest.TestCase):
    """Unittests for all feautures of the Console"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        self.std_out = StringIO()
        sys.stdout = self.std_out

    def tearDown(self):
        """Tear down console object"""
        self.std_out.close()
        sys.stdout = sys.__stdout__

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

        self.console.onecmd("quit")
        self.assertEqual(self.std_out.getvalue(), "")
