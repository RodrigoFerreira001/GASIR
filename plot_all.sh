#!/usr/bin/env bash
python plot_histogram.py moreno_highschool/G50P400/moreno_highschool_G50_P400_M5.result 70
python plot_histogram.py moreno_highschool/G50P400/moreno_highschool_G50_P400_M10.result 70
python plot_histogram.py moreno_highschool/G200P400/moreno_highschool_G200_P400_M5.result 70
python plot_histogram.py moreno_highschool/G200P400/moreno_highschool_G200_P400_M10.result 70

python plot_performance.py 100 50 moreno_highschool/G50P400/moreno_highschool_G50_P400_M5_generation_detailed.result moreno_highschool/G50P400/moreno_highschool_G50_P400_M5_detailed.result 70
python plot_performance.py 100 50 moreno_highschool/G50P400/moreno_highschool_G50_P400_M10_generation_detailed.result moreno_highschool/G50P400/moreno_highschool_G50_P400_M10_detailed.result 70
python plot_performance.py 100 200 moreno_highschool/G200P400/moreno_highschool_G200_P400_M5_generation_detailed.result moreno_highschool/G50P400/moreno_highschool_G50_P400_M5_detailed.result 70
python plot_performance.py 100 200 moreno_highschool/G200P400/moreno_highschool_G200_P400_M10_generation_detailed.result moreno_highschool/G50P400/moreno_highschool_G50_P400_M5_detailed.result 70
