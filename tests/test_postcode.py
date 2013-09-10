"""
Tests for postcode.py
"""
from .context import postcode
from postcode import *
from nose.tools import assert_equal, assert_raises

class TestCheckPostcodeFunc(object):
    # How to test?
    # Create a database fixture and checking that the
    # lookup works as expected?
    # Is this sufficient or do I need to mock every function call?
    def it_should_return_rows_for_postal_code_in_database(self):
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
    def it_should_raise_exception_for_more_than_one_result(self):
        result = [(u'TR', u'10000', u'Be\u015fpinar K\xf6y\xfc',
                   u'Balikesir', u'10', u'Balikesir', u'1',
                   u'K\xfcpeler(Ertu\u011frul)', u'52', 39.5, 27.81, 4),
                  (u'TR', u'10000', u'Beyk\xf6y K\xf6y\xfc', u'Balikesir',
                   u'10', u'Balikesir', u'1', u'K\xf6yler', u'45',
                   39.9499, 32.4414, 3),
                  (u'TR', u'10000', u'Yenice K\xf6y\xfc', u'Balikesir', u'10',
                   u'Balikesir', u'1', u'K\xf6yler', u'45', 40.25, 28.1333, 4)]
            #result = [(), ()]
        assert_raises(NonuniquePostcodeError, check_unique_postcode_data,
                      result)

    def it_should_not_raise_exception_for_zero_results(self):
        result = []
        check_unique_postcode_data(result)

    def it_should_not_raise_exception_for_one_result(self):
        result = [(u'GB', u'L3 5RF', u'Central Ward', u'England', u'ENG',
                   u'', u'', u'Liverpool District (B)',
                   u'E08000012', 53.4054171778326, -2.96977047535776, 6)]
        check_unique_postcode_data(result)

class TestUKPostcodeFunc(object):
    # Again, how to test with actual database lookup, fixture or mock
    def it_should_find_data_for_a_valid_UK_postcode(self):
        pass

class TestUSZipcodeFunc(object):
    # Again, how to test with actual database lookup, fixture or mock
    def it_should_cut_the_first_5_digits_from_a_9_digit_zip(self):
        pass

    def it_should_find_data_for_a_valid_zipcode(self):
        pass
