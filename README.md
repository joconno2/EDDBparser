# EDDBparser
A small python script that takes data in the form of JSON files from eddb.io and populates a SQLite database. Data is provided by users from the Elite: Dangerous video game.

USE
---
The script expects a systems.json and a stations_light.json in the working directory. these can be downloaded from the API page of eddb.io. When run, the script will create a db named eliteData.db, which is a SQLite database. I use SQLite Administrator to view the results, but any tool can be used to view and query the database.

TODO
---
Add support for commodities and the full stations data. From the full data, the 'listings' JSON array should be pulled out and built into a new table, which can then be joined as needed through the station_id key with teh stations table. Also build an interface to do anything that eddb.io may not do.