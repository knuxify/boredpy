# bored - a small utility that gives you ideas for things to do
# python rewrite

import os
import random

version = "py1"
# branch: master
# https://github.com/knuxify/boredpy

# List and counter locations

listfile = os.getenv("HOME") + "/.config/bored/ideas"
configfile = os.getenv("HOME") + "/.config/bored/config"

# Get counter
for confline in open(configfile):
	if "counter=" in confline:
		rawcounter=confline.replace("counter=", "")
		counter=int(rawcounter)

# Change counter by 1 and save it back to the config file
counter = counter + 1
for confline in open(configfile):
	if "counter=" not in confline:
		open(configfile, "w").write(confline + "\n")

open(configfile, "w").write("counter=" + str(counter))

# Get ID count
idcount = 0
for listline in open(listfile):
	idcount += listline.count("ID")

# Get random ID count
randomid = random.randint(1, idcount)

# Print everything and get the corresponding strings for the random ID
print("boredbutton version " + version + " | you've been bored " + str(counter) + " times")
print("So you're bored, right? How about you:")
foundline = 0
for line in open(listfile):
	if "ID" + str(randomid) in line:
		foundline = 1
	if foundline == 3:
		break
	if foundline > 0 and foundline <= 3 and "name=" in line:
		print(line.replace("name=", ""))
		foundline = foundline + 1
	if foundline > 0 and foundline <= 3 and "desc=" in line:
		print(line.replace("desc=", ""))
		foundline = foundline + 1
