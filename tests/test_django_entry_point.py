# -*- coding: utf-8 -*-
#
# tests - test_django_entry_point.py
#
# Philipp Meier - <pmeier82 at gmail dot com>
# 2011-11-01
#

"""unit tests for logging"""
__docformat__ = 'restructuredtext'


##---IMPORTS

try:
    # for python <= 2.7.x
    import unittest2 as unittest
except ImportError:
    import unittest


##---TESTS

class TestLogging(unittest.TestCase):
    """test case for logging"""

    def setUp(self):
        self.str_test = ['test1', 'test2', 'test3']

    def test_is_file_like(self):
        self.assertTrue(Logger.is_file_like(StringIO()))
        self.assertFalse(Logger.is_file_like(self))

    def test_logger_strio(self):
        """creating a logger for StringIO"""

        canvas = StringIO()
        logger = Logger.get_logger(canvas)
        test_str = ['test1', 'test2', 'test3']
        logger.log(*self.str_test)
        self.assertEqual(logger.get_content().split(), self.str_test)

    def test_delimiter_line(self):
        L = Logger(StringIO())
        L.log_delimiter_line()
        self.assertEqual(L.get_content().strip(), '*' * 20)

if __name__ == '__main__':
    unittest.main()