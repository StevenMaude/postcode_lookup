"""
Module for looking up postcodes from string.
"""

# TODO: write tests and test more thoroughly
import sqlite3


def check_postcode(postcode):
    """
    Take a potential postcode as string and return a tuple.

    First element is a boolean indicating whether string is a postcode,
    second and third elements are floats or None (if not a valid postcode).

    Returns (boolean, lat, lng).
    """
    # connect to SQL
    # is it better to reopen a connection every time we do a lookup
    # or to leave a connection open?
    conn = sqlite3.connect('test.sql')
    crsr = conn.cursor()

    # ensure postcode is upper case
    postcode = postcode.upper()

    # remove any whitespace
    postcode = ''.join(postcode.split())

    # create a tuple for insertion into SQL query
    postcode_term = (postcode,)

    # TODO: Rename postcode database
    crsr.execute("SELECT latitude, longitude FROM test \
                WHERE postcode=?", postcode_term)
    result = crsr.fetchone()
    
    if result is None:
        return (False, None, None)
    else:
        lat = result[0]
        lng = result[1]
        return (True, lat, lng)


def main():
    """
    Example postcode lookup
    """
    # try looking up ScraperWiki
    postcode = 'L3 5RF'
    print check_postcode(postcode)

if __name__ == '__main__':
    main()
