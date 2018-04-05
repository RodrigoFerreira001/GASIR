#!/usr/bin/env bash
for((number = 0; number < 100; number++)){
	python gasir_new.py watts_strogatz_500.txt 100 25 -f y
}

python plot_histogram.py watts_strogatz_500.result 500

for((number = 0; number < 100; number++)){
	python gasir_new.py watts_strogatz_1000.txt 100 50 -f y
}

python plot_histogram.py watts_strogatz_1000.result 1000


for((number = 0; number < 100; number++)){
	python gasir_new.py watts_strogatz_2000.txt 100 100 -f y
}

python plot_histogram.py watts_strogatz_2000.result 2000



python best_nodes_details.py watts_strogatz_500.sample watts_strogatz_500.txt
python best_nodes_details.py watts_strogatz_1000.sample watts_strogatz_1000.txt
python best_nodes_details.py watts_strogatz_2000.sample watts_strogatz_2000.txt

python plot_performance.py 100 100 watts_strogatz_500_generation_detailed.result watts_strogatz_500_detailed.result 500
python plot_performance.py 100 100 watts_strogatz_1000_generation_detailed.result watts_strogatz_1000_detailed.result 1000
python plot_performance.py 100 100 watts_strogatz_2000_generation_detailed.result watts_strogatz_2000_detailed.result 2000

python graph_info.py watts_strogatz_500.txt
python graph_info.py watts_strogatz_1000.txt
python graph_info.py watts_strogatz_2000.txt


