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

    def test_help_show(self):
        """Test help command"""
        
        output = "Prints the string representation of an instance\n"

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue(), output)

    def test_quit(self):
        """Test quit command"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")
