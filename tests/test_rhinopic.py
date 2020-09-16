# -*- coding: utf-8 -*-
"""Test of the rhinopic functions.

Those tests are patching
"""
import unittest
from unittest.mock import Mock, patch, mock_open
from pathlib import Path
import os
import sys

from rhinopics.rhinobuilder import RhinoBuilder
from rhinopics.rhinopic import Rhinopic


class TestRhinopic(unittest.TestCase):
    """
    Unittest of rhinopic functions.
    """
    BASE_PATH = Path('tests/fixtures/')
    IMGA_PATH = Path('tests/fixtures/imgA.JPG')
    IMGB_PATH = Path('tests/fixtures/imgB.jpg')

    def tearDown(self):
        """Reset the counter after each test."""
        Rhinopic.counter = 1

    def test_rename_pic_default(self):
        """
        Test the renaming of the files with default parameters.

        - Set the extension to lowercase.
        - Don't do a backup of the file.
        - Keyword is the parent directory.
        """
        n_digits = 1
        keyword = str(os.path.basename(os.getcwd()))
        backup = False
        lowercase = True
        with patch('pathlib.Path.replace') as replace:
            builder = RhinoBuilder(n_digits, keyword, backup, lowercase)
            rhino = builder.factory(self.IMGA_PATH)
            new_path = rhino.rename()
            self.assertEqual(new_path, self.BASE_PATH.joinpath('rhinopics_20191224_1.JPG'))

    def test_rename_pic_keyword_multiple_digits(self):
        """
        Test the renaming of the files.
        """
        n_digits = 4
        keyword = 'testA'
        backup = False
        lowercase = False
        with patch('pathlib.Path.replace') as replace:
            builder = RhinoBuilder(n_digits, keyword, backup, lowercase)
            rhino = builder.factory(self.IMGA_PATH)
            new_path = rhino.rename()
            self.assertEqual(new_path, self.BASE_PATH.joinpath('testA_20191224_0001.JPG'))

    def test_rename_pic_backup(self):
        """
        Test the renaming of the files.

        Test with a backup (copy) of the file.
        """
        n_digits = 1
        keyword = 'test_with_backup'
        backup = True
        lowercase = True
        with patch('builtins.open', unittest.mock.mock_open()):
            builder = RhinoBuilder(n_digits, keyword, backup, lowercase)
            rhino = builder.factory(self.IMGA_PATH)
            new_path = rhino.rename()
            self.assertEqual(new_path, self.BASE_PATH.joinpath('test_with_backup_20191224_1.JPG'))

    # TODO: check with files having the date in different fields.
    # TODO: unittest in another folder.


if __name__ == '__main__':
    from pkg_resources import load_entry_point
    sys.exit(load_entry_point('pytest', 'console_scripts', 'py.test')())  # type: ignore
