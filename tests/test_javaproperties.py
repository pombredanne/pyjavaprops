import os
from pyjavaprops.javaproperties import Properties
from pyjavaprops.settings.test import TEST_DATA_FOLDER

__author__ = 'luiscberrocal'

import unittest


class JavaPropertiesTestCase(unittest.TestCase):

    def setUp(self):
        filename = os.path.join(TEST_DATA_FOLDER, 'complex.properties')
        self.java_properties = Properties()
        self.java_properties.load(open(filename))

    def test_value_with_spaces(self):
        self.assertEqual('Value14 With Spaces', self.java_properties['Key14'])
        self.assertEqual('Value01-test', self.java_properties['Key23'])

    def test_variable(self):
        self.assertEqual('Value01-test', self.java_properties['Key23'])

    def test_variable_dollar(self):
        self.assertEqual('', self.java_properties['Key24'])


if __name__ == '__main__':
    unittest.main()
