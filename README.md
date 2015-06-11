# EDDBparser
A small python script that takes data in the form of JSON files from eddb.io and populates a SQLite database. Data is provided by users from the Elite: Dangerous video game.

USE
---
The script expects a systems.json and a stations.json in the working directory. these can be downloaded from the API page of eddb.io. When run, the script will create a db named eliteData.db, which is a SQLite database. I use SQLite Administrator to view the results, but any tool can be used to view and query the database.

TODO
---
Add support for commodities and build an interface to do anything that eddb.io may not do.