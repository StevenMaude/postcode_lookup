"""
Module for looking up postcodes from string.
"""

# TODO: write tests and test more thoroughly
import sqlite3


def check_postcode(postcode, country_code, dbse='allCountries.sqlite'):
    # TODO: check what this returns
    """
    Take a potential postcode as string and return a list of tuples.
    
    Geonames database is structured as country_code, postal_code, place_name,
    admin_name1, admin_code1, admin_name2, admin_code2, admin_name3,
    admin_code3, latitude, longitude, accuracy.

    Latitude, longitude should be handled as floats, accuray as an int,
    the other columns are strings.

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


def tidy_postcode(postcode):
    """
    Return a postcode string as upper case, remove any whitespace before and
    after postcode.
    """
    return postcode.upper().strip()


def uk_postcode(postcode):
    """
    Look up data for a UK postcode provided as string with a single
    whitespace between the outcode and incode.
    """
    postcode = tidy_postcode(postcode)
    uk_fullcode_lookup = check_postcode(postcode, 'GB')
    check_unique_postcode_data(uk_fullcode_lookup)
    # combine data from outcode and full postcode
    uk_outcode_lookup = check_postcode(postcode.split()[0], 'GB')
    combined_lookup = uk_outcode_lookup[0][:-3] + uk_fullcode_lookup[0][-3:]

    # return uk_fullcode_lookup, uk_outcode_lookup, combined_lookup
    return [combined_lookup]

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
