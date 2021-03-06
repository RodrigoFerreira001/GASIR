import os

graph = open("moreno_health.txt", "r")
ef = graph.read()

pop = ["50","100","200"]
gen = ["50", "100", "200"]
mut = ["1","5","10"]

for p in pop:
	for g in gen:
		for m in mut:
			if not os.path.exists(str("G" + g + "P" + p)):
				os.makedirs(str("G" + g + "P" + p))

			filename = "G" + g + "P" + p + "/moreno_health_" + "G" + g + "_P" + p + "_M" + m + ".txt"
			of = open(filename, "w")
			of.write(ef)
			of.close()

			print "# G " + g + " P " + p + "M " + m
			print "for((number = 0; number < 100; number++)){"
			print "\t python gasir.py moreno_health/" + filename + " " + p + " 127 --mutation " +  str(int(m) / 100.0) + " --generations " + g
			print "}\n\n"
