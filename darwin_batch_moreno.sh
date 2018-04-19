#!/usr/bin/env bash

#G 50 P 200 M 1
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G50P200/moreno_health_G50_P200_M1.txt 200 127 --mutation 0.01 --generations 50
}

#G 50 P 200 M 5
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G50P200/moreno_health_G50_P200_M5.txt 200 127 --mutation 0.05 --generations 50
}

#G 50 P 200 M 10
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G50P200/moreno_health_G50_P200_M10.txt 200 127 --mutation 0.1 --generations 50
}

########################

#G 100 P 100 M 1
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G100P100/moreno_health_G100_P100_M1.txt 100 127 --mutation 0.01 --generations 100
}

#G 100 P 100 M 5
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G100P100/moreno_health_G100_P100_M5.txt 100 127 --mutation 0.05 --generations 100
}

#G 100 P 100 M 10
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G100P100/moreno_health_G100_P100_M10.txt 100 127 --mutation 0.1 --generations 100
}

########################

#G 200 P 50 M 1
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G200P50/moreno_health_G200_P50_M1.txt 50 127 --mutation 0.01 --generations 200
}

#G 200 P 50 M 5
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G200P50/moreno_health_G200_P50_M5.txt 50 127 --mutation 0.5 --generations 200
}

#G 200 P 50 M 10
for((number = 0; number < 5; number++)){
	python gasir.py moreno_health/G200P50/moreno_health_G200_P50_M10.txt 50 127 --mutation 0.1 --generations 200
}