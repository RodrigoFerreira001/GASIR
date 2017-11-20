#python plot_histogram.py erdos_renyi_500.result 500
#python plot_histogram.py watts_strogatz_500.result 500
#python plot_histogram.py erdos_renyi_1000.result 1000
#python plot_histogram.py watts_strogatz_1000.result 1000
#python plot_histogram.py erdos_renyi_2000.result 2000
#python plot_histogram.py watts_strogatz_2000.result 2000

python plot_performance.py 10 100 erdos_renyi_500_generation_detailed.result erdos_renyi_500_detailed.result 500

python plot_performance.py 10 100 erdos_renyi_1000_generation_detailed.result erdos_renyi_1000_detailed.result 1000

python plot_performance.py 10 100 erdos_renyi_2000_generation_detailed.result erdos_renyi_2000_detailed.result 2000

python plot_performance.py 10 100 watts_strogatz_500_generation_detailed.result watts_strogatz_500_detailed.result 500

python plot_performance.py 10 100 watts_strogatz_1000_generation_detailed.result watts_strogatz_1000_detailed.result 1000

python plot_performance.py 10 100 watts_strogatz_2000_generation_detailed.result watts_strogatz_2000_detailed.result 2000
