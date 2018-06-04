#!/usr/bin/env bash
# cagrqc
for((number = 0; number < 10; number++)){
         python gasir.py redes/cagrqc/cagrqc.txt 200 262 --mutation 0.05 --generations 50
}

# email_enron
for((number = 0; number < 10; number++)){
         python gasir.py redes/email_enron/email_enron.txt 200 1834 --mutation 0.05 --generations 50
}

# hep
for((number = 0; number < 10; number++)){
         python gasir.py redes/hep/hep.txt  200 761 --mutation 0.05 --generations 50
}

# phy
for((number = 0; number < 10; number++)){
         python gasir.py redes/phy/phy.txt  200 1857 --mutation 0.05 --generations 50
}

# Slashdot0811
for((number = 0; number < 10; number++)){
         python gasir.py redes/Slashdot0811/Slashdot0811.txt  200 3868 --mutation 0.05 --generations 50
}


