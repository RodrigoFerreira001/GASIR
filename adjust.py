# -*- coding: utf-8 -*-
import sys
linhas = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")

for line in linhas.readlines():
	tmp = line.replace("\n","").split("\t")
	output.write( str(int(tmp[0]) - 1) + " " + str(int(tmp[1]) - 1) + "\n")


output.close()
