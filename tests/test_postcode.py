"""
Tests for postcode.py
"""
from .context import postcode
from postcode import tidy_postcode
from nose.tools import assert_equal


class TestTidyPostcodeFunc(object):
    def it_should_change_lower_case_to_upper_case(self):
        testcode = 'l3 5rf'
        result = tidy_postcode(testcode)
        assert_equal(result, 'L3 5RF')

    def it_should_not_change_upper_case(self):
        testcode = 'L3 5RF'
        result = tidy_postcode(testcode)
        assert_equal(result, 'L3 5RF')

    def it_should_strip_left_whitespace(self):
        testcode = '\t  50000'
        result = tidy_postcode(testcode)
        assert_equal(result, '50000')
    
    def it_should_strip_right_whitespace(self):
        testcode = '30000  \n\t  '
        result = tidy_postcode(testcode)
        assert_equal(result, '30000')

class TestUKPostcodeFunc(object):
    pass
