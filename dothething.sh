for((number = 0; number < 100; number++)){
	python gasir.py sociopatterns_0_005.txt 100 30 --infecteds 5 122
}

python plot_histogram.py sociopatterns_0_005.result 410


for((number = 0; number < 100; number++)){
	python gasir.py sociopatterns_0_01.txt 100 30 --infecteds 406 82 156 228
}

python plot_histogram.py sociopatterns_0_01.result 410


for((number = 0; number < 100; number++)){
	python gasir.py sociopatterns_0_05.txt 100 30 --infecteds 375 219 356 180 197 130 214 69 328 107 224 251 361 377 344 384 346 16 169 350
}

python plot_histogram.py sociopatterns_0_05.result 410

exit 0
