
Assumes you have an SQLite database that has columns postal code, latitude and longitude.

I'm using the [geonames](http://download.geonames.org/export/zip/) databases converted to SQLite with the commands
below:

    sqlite3 geonames.db
    sqlite> CREATE TABLE geonames (country_code TEXT, postal_code TEXT, place_name TEXT, admin_name1 TEXT, admin_code1 TEXT,
admin_name2 TEXT, admin_code2 TEXT, admin_name3 TEXT, admin_code3 TEXT, latitude REAL, longitude REAL, accuracy
NUMERIC);
    sqlite> .separator \t
    sqlite> .import geonames_allCountries.txt geonames
    sqlite> .exit
