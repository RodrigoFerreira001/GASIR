for((number = 0; number < 10; number++)){
	python gasir_new.py erdos_renyi_500.txt 100 25
}

python plot_histogram.py erdos_renyi_500.result 500

for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_500.txt 100 25
}

python plot_histogram.py watts_strogatz_500.result 500

for((number = 0; number < 10; number++)){
	python gasir_new.py erdos_renyi_1000.txt 100 50
}

python plot_histogram.py erdos_renyi_1000.result 1000

for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_1000.txt 100 50
}

python plot_histogram.py watts_strogatz_1000.result 1000


for((number = 0; number < 10; number++)){
	python gasir_new.py erdos_renyi_2000.txt 100 100
}

python plot_histogram.py erdos_renyi_2000.result 2000

for((number = 0; number < 10; number++)){
	python gasir_new.py watts_strogatz_2000.txt 100 100
}

python plot_histogram.py watts_strogatz_2000.result 2000