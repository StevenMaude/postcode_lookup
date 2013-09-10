"""
Module for looking up postcodes from string.
"""

# TODO: write tests and test more thoroughly
import sqlite3

#def get_first_table_name(db):
#    """
#    Return first table from a SQLite database as unicode.
#    """
#    conn = sqlite3.connect(db)
#    crsr = conn.cursor()
#    crsr.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
#    name = crsr.fetchall()[0][0]
#    conn.close()
#   return name


def check_postcode(dbse, postcode):
    """
    Take a potential postcode as string and return a tuple.

    Assume that the postcode is upper case (if alpha) and that any preceding
    and following whitespace is stripped.

    First element is a boolean indicating whether string is a postcode,
    second and third elements are latitude and longitude, provided as
    floats or None (if not a valid postcode).

    Returns (boolean, lat, lng).
    """
    # connect to SQL
    # is it better to reopen a connection every time we do a lookup
    # or to leave a connection open?
    conn = sqlite3.connect(dbse)
    crsr = conn.cursor()

    # remove any whitespace
    # postcode = ''.join(postcode.split())

    # create a tuple for insertion into SQL query
    query = (postcode, )

    # TODO: Rename postcode database
    # can't parametrize table name and bad to use string operations
    # to generate SQL queries as can be open to injection
    crsr.execute("SELECT * FROM geonames WHERE postal_code=?", query)
    result = crsr.fetchall()
    return result
   # if result is None:
   #     return (False, None, None)
   # else:
   #     lat = float(result[0])
   #     lng = float(result[1])
   #     return (True, lat, lng)


class NonuniquePostcodeError(Exception):
    """
    For cases where a postcode lookup returns more than one result.
    """
    pass


def main():
    """
    Example postcode lookup
    """
    # try looking up ScraperWiki
    # postcode = 'L3 5RF'
    # print check_postcode(postcode)
    dbse = 'allCountries.sqlite'
    # tb_name = get_first_table_name(db)
    # print tb_name
    results = check_postcode(dbse, 'L3')
    if len(results) > 1:
        raise NonuniquePostcodeError("Postal code is not unique.")

    for result in results:
        print result


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
    pass


def us_zipcode(zipcode):
    """
    Look up ZIP code data for a 5 digit US ZIP code provided as a string.
    (Geonames DB only seems to include 5 digit codes at the moment.)
    """
    # check length, want to drop any digits after dash as these aren't
    # included
    pass

if __name__ == '__main__':
    main()
