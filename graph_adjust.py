# -*- coding: utf-8 -*-
import sys

gf = open(sys.argv[1], "r")
fo = open(str(sys.argv[1].split(".")[0] + "_ad.txt"), "w")

for line in gf.readlines():
	values = line.split(" ")
	fo.write( str(int(values[0]) - 1) + " " + str(int(values[1]) - 1) + "\n")
	print str(int(values[0]) - 1) + " " + str(int(values[1]) - 1)
