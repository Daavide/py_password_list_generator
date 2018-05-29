#!/usr/bin/python

#by dmagni, 16 apr 2018

import sys
import os

print "Python Simple string 'combinator'"

if len(sys.argv) == 2:

	if sys.argv[1] == "--help":
		print "Specify 2 or 3 input file as arguments. Example: script.py file1.txt file2.txt file3.txt "

	else:
		print "Invalid arguments number; please use --help for help"

elif len(sys.argv) == 4:

	try:
		file1 = open(sys.argv[1],"r")
	except Exception as e:
		print "Error opening file " + sys.argv[1]
		print e
		quit()

	try:
		file2 = open(sys.argv[2],"r")
	except Exception as e:
		print "Error opening file " + sys.argv[2]
		print e
		quit()

	try:
		file3 = open(sys.argv[3],"r")
	except Exception as e:
		print "Error opening file " + sys.argv[3]
		print e
		quit()

	list1 = file1.readlines()
	list2 = file2.readlines()
	list3 = file3.readlines()

	for element1 in list1:
	     for element2 in list2:
	          for element3 in list3:
	          	   os.system("echo " + element1.strip("\n") + element2.strip("\n") + element3.strip("\n") + " >> output.txt" )
	               #print element1.strip("\n") + element2.strip("\n") + element3.strip("\n")

	print "OK. Lines in output: "
	os.system("cat output.txt | wc -l")


elif len(sys.argv) == 3:

	try:
		file1 = open(sys.argv[1],"r")
	except Exception as e:
		print "Error opening file " + sys.argv[1]
		print e
		quit()

	try:
		file2 = open(sys.argv[2],"r")
	except Exception as e:
		print "Error opening file " + sys.argv[2]
		print e
		quit()

	list1 = file1.readlines()
	list2 = file2.readlines()

	for element1 in list1:
	     for element2 in list2:
	     	os.system("echo " + element1.strip("\n") + element2.strip("\n") + " >> output.txt" )
	        #print element1.strip("\n") + element2.strip("\n")

	print "OK. Lines in output: "
	os.system("cat output.txt | wc -l")

else:
	print "Invalid arguments number; please use --help for help"


