for((number = 0; number < 100; number++)){
	python gasir_new.py sociopatterns_0_005.txt 100 30 -p 0.005
}

python plot_histogram.py sociopatterns_0_005.result 410

for((number = 0; number < 100; number++)){
	python gasir_new.py sociopatterns_0_01.txt 100 30 -p 0.01
}

python plot_histogram.py sociopatterns_0_01.result 410

for((number = 0; number < 100; number++)){
	python gasir_new.py sociopatterns_0_05.txt 100 30 -p 0.05
}

python plot_histogram.py sociopatterns_0_05.result 410

exit 0
