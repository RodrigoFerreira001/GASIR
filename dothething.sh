for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_500.txt 100 25 --infecteds 228 274 293 343 422 465
}

python plot_histogram.py watts_strogatz_500.result 500

for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_1000.txt 100 50 --infecteds 24 26 47 151 204 231 276 277 289 309 329 383 436 450 451 474 495 534 645 743 756 782 783 790 957
}

python plot_histogram.py watts_strogatz_1000.result 1000


for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_2000.txt 100 100 --infecteds 15 51 154 173 260 384 544 611 617 638 639 641 809 823 854 948 966 1057 1061 1070 1079 1081 1192 1200 1214 1245 1484 1509 1628 1714 1734 1764 1854 1876 1918 1926
}

python plot_histogram.py watts_strogatz_2000.result 2000