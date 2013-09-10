"""
Module for looking up postcodes from string.
"""

# TODO: write tests and test more thoroughly
import sqlite3


def check_postcode(postcode, country_code, dbse='allCountries.sqlite'):
    # TODO: check what this returns
    """
    Take a potential postcode as string and return a tuple.

    Assume that the postcode is upper case (if alpha) and that any preceding
    and following whitespace is stripped.

    First element is a boolean indicating whether string is a postcode,
    second and third elements are latitude and longitude, provided as
    floats or None (if not a valid postcode).
    """
    # connect to SQL
    # is it better to reopen a connection every time we do a lookup
    # or to leave a connection open?
    conn = sqlite3.connect(dbse)
    crsr = conn.cursor()

    # create a tuple for insertion into SQL query
    query = (postcode, country_code)

    # TODO: Rename postcode database
    # can't parametrize table name and bad to use string operations
    # to generate SQL queries as can be open to injection
    crsr.execute("SELECT * FROM geonames WHERE postal_code=? AND country_code \
            =?", query)
    result = crsr.fetchall()
    return result


class NonuniquePostcodeError(Exception):
    """
    For cases where a postcode lookup returns more than one result.
    """
    pass


def check_unique_postcode_data(result):
    """
    Check if we only have one unique postcode result from database lookup.
    """
    # if looking for UK or US postcodes, should only find one entry in
    # database
    # for other countries, this may not be true
    if len(result) > 1:
        raise NonuniquePostcodeError("Postal code is not unique.")


def main():
    """
    Example postcode lookup
    """
    # try looking up ScraperWiki
    # postcode = 'L3 5RF'
    # print check_postcode(postcode)
    # tb_name = get_first_table_name(db)
    # print tb_name

    print us_zipcode('90210')
    print uk_postcode('L3 5RF')
    print uk_postcode('L3')


def tidy_postcode(postcode):
    """
    Return a postcode string as upper case, remove any whitespace before and
    after postcode.
    """
    return postcode.upper().lstrip().rstrip()


def uk_postcode(postcode):
    """
    Look up data for a UK postcode provided as string with a single
    whitespace between the outcode and incode.
    """
    postcode = tidy_postcode(postcode)
    uk_lookup = check_postcode(postcode, 'GB')
    check_unique_postcode_data(uk_lookup)
    return uk_lookup


def us_zipcode(zipcode):
    """
    Look up ZIP code data for a 5 digit US ZIP code provided as a string.
    (Geonames DB only seems to include 5 digit codes at the moment.)
    """
    # check length, want to drop any digits after dash as these aren't
    # included
    zipcode = tidy_postcode(zipcode)
    us_lookup = check_postcode(zipcode, 'US')
    check_unique_postcode_data(us_lookup)
    return us_lookup

if __name__ == '__main__':
    main()
