for((number = 0; number < 100; number++)){
	python gasir.py sociopatterns_0_005.txt 100 30 -p 0.005
}

python plot_histogram.py sociopatterns_0_005.result 410


exit 0
