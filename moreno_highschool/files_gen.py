import os

#graph = open("moreno_highschool.txt", "r")
#ef = graph.read()

pop = ["50", "100", "200"]
gen = ["50", "100", "200"]
mut = ["1", "5", "10"]

for p in pop:
	for g in gen:
		for m in mut:
			# if not os.path.exists(str("G" + g + "P" + p)):
			# 	os.makedirs(str("G" + g + "P" + p))

			filename = "G" + g + "P" + p + "/moreno_highschool_" + "G" + g + "_P" + p + "_M" + m
			#of = open(filename + ".txt", "w")
			#of.write(ef)
			#of.close()

			# print "# G " + g + " P " + p + "M " + m
			# print "for((number = 0; number < 100; number++)){"
			# print "\t python gasir.py moreno_highschool/" + filename + " " + p + " 8 --mutation " +  str(int(m) / 100.0) + " --generations " + g + " --infecteds 21"
			# print "}\n\n"

			print "python plot_histogram.py moreno_highschool/" + filename + ".result 70"
			print "python plot_performance.py 100 " + str(g) + " moreno_highschool/" + filename + "_generation_detailed.result" + " moreno_highschool/" + filename + "_detailed.result 70"
