#!/usr/bin/env bash
for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_500.txt 100 25 -p 0.05 -f y --infecteds 25 132 259 260 300 467
}

python plot_histogram.py watts_strogatz_500.result 500

for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_1000.txt 100 50 -p 0.05 -f y --infecteds 24 143 196 232 411 487 515 572 597 602 606 639 925 926
}

python plot_histogram.py watts_strogatz_1000.result 1000


for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_2000.txt 100 100 -p 0.05 -f y --infecteds 14 113 233 388 408 471 486 513 582 588 664 817 824 854 898 962 1003 1086 1095 1142 1300 1410 1597 1792 1885 1894 1912 1931
}

python plot_histogram.py watts_strogatz_2000.result 2000



python best_nodes_details.py watts_strogatz_500.sample watts_strogatz_500.txt
python best_nodes_details.py watts_strogatz_1000.sample watts_strogatz_1000.txt
python best_nodes_details.py watts_strogatz_2000.sample watts_strogatz_2000.txt

python plot_performance.py 10 100 watts_strogatz_500_generation_detailed.result watts_strogatz_500_detailed.result 500
python plot_performance.py 10 100 watts_strogatz_1000_generation_detailed.result watts_strogatz_1000_detailed.result 1000
python plot_performance.py 10 100 watts_strogatz_2000_generation_detailed.result watts_strogatz_2000_detailed.result 2000

python graph_info.py watts_strogatz_500.txt
python graph_info.py watts_strogatz_1000.txt
python graph_info.py watts_strogatz_2000.txt