# Jim O'Connor
# 6/11/2015
# 
# Populates a SQLite database from EDDB system and station data


import json
import sqlite3
from os import remove
from os import path
from collections import OrderedDict

#parses the data from a supplied systems.json
def getData(fileName,recordNumber):

	file = open(fileName,'r')
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
			if not(isinstance(subitem[1], (str,int))):
				stripped_list.append(str(subitem[1]))
			else:
				stripped_list.append(subitem[1])

	for i in range(0, len(stripped_list), recordNumber):
		results_list.append(tuple(stripped_list[i:i+recordNumber]))
	
	return results_list
	


	
def main():
	#clean up any existing DB and create the new one
	
	if path.isfile("eliteData.db"):
		remove("eliteData.db")
	
	conn = sqlite3.connect("eliteData.db")
 
	cursor = conn.cursor()

	cursor.execute("""CREATE TABLE systems
                  (id,name,x,y,z,faction,population,goverment,allegiance,
				  state,security,primary_economy,needs_permit,updated_at) 
               """)
	cursor.execute("""CREATE TABLE stations
                  (id,name,system_id,max_landing_pad_size,distance_to_star,
				  faction,government,allegiance,state,type,has_blackmarket,
				  has_commodities,has_refuel,has_repair,has_rearm,
				  has_outfitting,has_shipyard,import_commodities,
				  export_commodities,prohibited_commodities,economies,
				  updated_at) 
               """)
			
	#get the data from the previous function and populate the DB
	systemData = getData('systems.json',14)
	stationData = getData('stations.json',22)
	cursor.executemany("INSERT INTO systems VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (systemData))
	cursor.executemany("INSERT INTO stations VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (stationData))
	conn.commit()
main()
