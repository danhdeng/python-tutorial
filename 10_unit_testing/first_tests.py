# Unit testing is a way to teswt individual untis of code
# - Typincally automated
#  - Gain confidence that individual parts of our software is working.
#  - keep part of refactoring
# 
#

import unittest

# define a class extends unittest.TestCase
class TestStringOperations(unittest.TestCase):
    # write out tests...
    def test_length_dan_is_3(self):
        name='dan'
        self.assertEqual(len(name), 3)

    def test_x_not_in_string(self):
        sentence="On Earth, gravity gives weight to physical objects, and the moon's gravity causes the ocean tides"
        is_x_in_sentence='x' in sentence
        self.assertFalse(is_x_in_sentence)


if __name__ == '__main__':
    unittest.main()