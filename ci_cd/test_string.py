#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
"""test"""

import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        """test upper"""
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """test is upper"""
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """test split"""
        statment = 'hello world'
        self.assertEqual(statment.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            statment.split(2)


if __name__ == '__main__':
    unittest.main()
