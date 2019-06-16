#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import unittest


class Calculate(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def sum(self):
        return self._x + self._y

    def min(self):
        return self._x - self._y


class CalculateTestCase(unittest.TestCase):

    def setUp(self):
        self._calculate = Calculate(1,2)

    def tearDown(self):
        self._calculate = None

    def test_sum(self):
        self.assertEqual(self._calculate.sum(), 3)

    def test_min(self):
        self.assertEqual(self._calculate.min(), -1)


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(CalculateTestCase('test_sum'))
    test_suite.addTest(CalculateTestCase('test_min'))
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)

