#!/usr/bin/python

#   Copyright 2017 John Bailey
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import unittest
import varints

class TestStringMethods(unittest.TestCase):

    """ Test the LEB128 varint format, using passing None """
    def test_leb128_none(self):
        test_data = None
        expected_result = None

        ascii_result = varints.leb128.encode(test_data)
        num_result = varints.leb128.decode(ascii_result)

        self.assertEqual(ascii_result,expected_result)
        self.assertEqual(num_result,test_data)

    """ Test the LEB128 varint format, using a value of zero """
    def test_leb128_single_number_zero(self):
        test_data = 0
        expected_result = varints.varint_storage(0)

        ascii_result = varints.leb128.encode(test_data)
        num_result = varints.leb128.decode(ascii_result)

        self.assertEqual(ascii_result,expected_result)
        self.assertEqual(num_result,test_data)

    """ Test the LEB128 varint format, using minimum non-zero value """
    def test_leb128_single_number_non_zero(self):
        test_data = 1
        expected_result = varints.varint_storage(1)

        ascii_result = varints.leb128.encode(test_data)
        num_result = varints.leb128.decode(ascii_result)

        self.assertEqual(ascii_result,expected_result)
        self.assertEqual(num_result,test_data)

    """ Test the LEB128 varint format, using max value which can be stored in a single byte """
    def test_leb128_single_number_max(self):
        test_data = 127
        expected_result = varints.varint_storage(127)

        ascii_result = varints.leb128.encode(test_data)
        num_result = varints.leb128.decode(ascii_result)

        self.assertEqual(ascii_result,expected_result)
        self.assertEqual(num_result,test_data)

    """ Test the LEB128 varint format, using minimum value necessary for 2 byte
        storage"""
    def test_leb128_two_number_min(self):
        test_data = 128
        expected_result = varints.varint_storage(128) + \
                          varints.varint_storage(1)

        ascii_result = varints.leb128.encode(test_data)
        num_result = varints.leb128.decode(ascii_result)

        self.assertEqual(ascii_result,expected_result)
        self.assertEqual(num_result,test_data)


if __name__ == '__main__':
    unittest.main()
