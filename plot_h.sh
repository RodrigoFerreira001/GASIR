#!/usr/bin/env bash
python plot_performance.py 10 100 watts_strogatz_500_generation_detailed.result watts_strogatz_500_detailed.result 500

python plot_performance.py 10 100 watts_strogatz_1000_generation_detailed.result watts_strogatz_1000_detailed.result 1000

python plot_performance.py 10 100 watts_strogatz_2000_generation_detailed.result watts_strogatz_2000_detailed.result 2000
