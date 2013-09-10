"""
Tests for postcode.py
"""
from .context import postcode
from postcode import tidy_postcode
from nose.tools import assert_equal

class TestCheckPostcodeFunc(object):
    pass

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

    def it_should_strip_left_and_right_whitespace(self):
        testcode = '  \n\t  L3 5RF    \t\t\n\t '
        result = tidy_postcode(testcode)
        assert_equal(result, 'L3 5RF')

class TestCheckUniquePostcodeDataFunc(object):
    def it_should_raise_exception_for_more_than_one_result():
        pass

    def it_should_not_raise_exception_for_zero_results():
        pass

    def it_should_not_raise_exception_for_one_result():
        pass

class TestUKPostcodeFunc(object):
    pass
