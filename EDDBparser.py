# Jim O'Connor
# 6/11/2015
# 
# Populates a SQLite database from EDDB system data


import json
import sqlite3
from os import remove
from collections import OrderedDict

#parses the data from a supplied systems.json
def getData():

	file = open('systems.json','r')
	fileString = file.read()
	file.close()

	#allows the dict tht the json is loaded into to stay sorted
	write_data = OrderedDict([
		('a', '1'),
		('b', '2'),
		('c', '3')
	]	)

	#I should cut down the number of lists and do these in place
	parsed_json = json.loads(fileString,object_pairs_hook=OrderedDict)
	json_list = []
	stripped_list = []
	results_list = []
	db_list = []

	for item in parsed_json:
		json_list.append(list(item.items()))
		
	for item in json_list:
		for subitem in item:
			stripped_list.append(subitem[1])

	for i in range(0, len(stripped_list), 14):
		results_list.append(tuple(stripped_list[i:i+14]))
	
	return results_list
	


	
def main():
	#clean up any existing DB and create the new one
	remove("systemData.db")
	conn = sqlite3.connect("systemData.db")
 
	cursor = conn.cursor()

	cursor.execute("""CREATE TABLE systems
                  (id,name,x,y,z,faction,population,goverment,allegiance,
				  state,security,primary_economy,needs_permit,updated_at) 
               """)
			
	#get the data from the previous function and populate the DB
	systemData = getData()
	cursor.executemany("INSERT INTO systems VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (systemData))
	conn.commit()
main()
