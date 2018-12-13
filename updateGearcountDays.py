#!/usr/bin/python

import MySQLdb
import calendar

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="new_excursion")
cur = db.cursor()

while True:
	day_o_week= input("Please enter the day of the week (0 is Monday, 6 is Sunday, 69 to exit) >")
	if day_o_week not in range(7):
		exit()
	staff_phone= raw_input("Please enter the phone of the gear-counting staff >")


	cur.execute("SELECT fullname, email FROM user WHERE phone='{}'".format(staff_phone))
	print "Is this the Staff you want to count on {}?".format(calendar.day_name[day_o_week])
	result=cur.fetchall()[0]
	print "  {}".format(result)
	proceed = raw_input("Type yes to proceed > ")

	if proceed != "yes":
	    exit()

	with open('/home/blake/excursion/yassine/gearcountdays.txt') as file:
		data =file.readlines()

	data[day_o_week] = result[1] + '\n'

	with open('/home/blake/excursion/yassine/gearcountdays.txt', 'w') as file:
		file.writelines( data )

	print "{} has to count gear on {} or buy board a six pack!".format(result[0],calendar.day_name[day_o_week])



print "Finished"
