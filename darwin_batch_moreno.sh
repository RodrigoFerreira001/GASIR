#!/usr/bin/env bash

# G 50 P 50M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G50P50/moreno_health_G50_P50_M1.txt 50 127 --mutation 0.01 --generations 50
}


# G 50 P 50M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G50P50/moreno_health_G50_P50_M5.txt 50 127 --mutation 0.05 --generations 50
}


# G 50 P 50M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G50P50/moreno_health_G50_P50_M10.txt 50 127 --mutation 0.1 --generations 50
}


# G 100 P 50M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G100P50/moreno_health_G100_P50_M1.txt 50 127 --mutation 0.01 --generations 100
}


# G 100 P 50M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G100P50/moreno_health_G100_P50_M5.txt 50 127 --mutation 0.05 --generations 100
}


# G 100 P 50M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G100P50/moreno_health_G100_P50_M10.txt 50 127 --mutation 0.1 --generations 100
}


# G 200 P 50M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G200P50/moreno_health_G200_P50_M1.txt 50 127 --mutation 0.01 --generations 200
}


# G 200 P 50M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G200P50/moreno_health_G200_P50_M5.txt 50 127 --mutation 0.05 --generations 200
}


# G 200 P 50M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G200P50/moreno_health_G200_P50_M10.txt 50 127 --mutation 0.1 --generations 200
}


# G 50 P 100M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G50P100/moreno_health_G50_P100_M1.txt 100 127 --mutation 0.01 --generations 50
}


# G 50 P 100M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G50P100/moreno_health_G50_P100_M5.txt 100 127 --mutation 0.05 --generations 50
}


# G 50 P 100M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G50P100/moreno_health_G50_P100_M10.txt 100 127 --mutation 0.1 --generations 50
}


# G 100 P 100M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G100P100/moreno_health_G100_P100_M1.txt 100 127 --mutation 0.01 --generations 100
}


# G 100 P 100M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G100P100/moreno_health_G100_P100_M5.txt 100 127 --mutation 0.05 --generations 100
}


# G 100 P 100M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G100P100/moreno_health_G100_P100_M10.txt 100 127 --mutation 0.1 --generations 100
}


# G 200 P 100M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G200P100/moreno_health_G200_P100_M1.txt 100 127 --mutation 0.01 --generations 200
}


# G 200 P 100M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G200P100/moreno_health_G200_P100_M5.txt 100 127 --mutation 0.05 --generations 200
}


# G 200 P 100M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G200P100/moreno_health_G200_P100_M10.txt 100 127 --mutation 0.1 --generations 200
}


# G 50 P 200M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G50P200/moreno_health_G50_P200_M1.txt 200 127 --mutation 0.01 --generations 50
}


# G 50 P 200M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G50P200/moreno_health_G50_P200_M5.txt 200 127 --mutation 0.05 --generations 50
}


# G 50 P 200M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G50P200/moreno_health_G50_P200_M10.txt 200 127 --mutation 0.1 --generations 50
}


# G 100 P 200M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G100P200/moreno_health_G100_P200_M1.txt 200 127 --mutation 0.01 --generations 100
}


# G 100 P 200M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G100P200/moreno_health_G100_P200_M5.txt 200 127 --mutation 0.05 --generations 100
}


# G 100 P 200M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G100P200/moreno_health_G100_P200_M10.txt 200 127 --mutation 0.1 --generations 100
}


# G 200 P 200M 1
for((number = 0; number < 100; number++)){
	 python gasir.py G200P200/moreno_health_G200_P200_M1.txt 200 127 --mutation 0.01 --generations 200
}


# G 200 P 200M 5
for((number = 0; number < 100; number++)){
	 python gasir.py G200P200/moreno_health_G200_P200_M5.txt 200 127 --mutation 0.05 --generations 200
}


# G 200 P 200M 10
for((number = 0; number < 100; number++)){
	 python gasir.py G200P200/moreno_health_G200_P200_M10.txt 200 127 --mutation 0.1 --generations 200
}
