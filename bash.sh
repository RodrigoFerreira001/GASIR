#!/usr/bin/env bash
# G 50 P 400M 5
for((number = 0; number < 100; number++)){
         python gasir.py moreno_highschool/G50P400/moreno_highschool_G50_P400_M5.txt 400 8 --mutation 0.05 --generations 50 --infecteds 21
}


# G 50 P 400M 10
for((number = 0; number < 100; number++)){
         python gasir.py moreno_highschool/G50P400/moreno_highschool_G50_P400_M10.txt 400 8 --mutation 0.1 --generations 50 --infecteds 21
}


# G 200 P 400M 5
for((number = 0; number < 100; number++)){
         python gasir.py moreno_highschool/G200P400/moreno_highschool_G200_P400_M5.txt 400 8 --mutation 0.05 --generations 200 --infecteds 21
}


# G 200 P 400M 10
for((number = 0; number < 100; number++)){
         python gasir.py moreno_highschool/G200P400/moreno_highschool_G200_P400_M10.txt 400 8 --mutation 0.1 --generations 200 --infecteds 21
}
