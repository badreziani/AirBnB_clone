#!/usr/bin/python3
"""This module contains test suits"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Unittests for all feautures of the Console"""

    def test_help(self):
        """Test the help method"""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

        help_string = "Prints the string representation of an instance"

        self.assertTrue(f.getvalue(), help_string)
