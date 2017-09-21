for((number = 0; number < 70; number++)){
	python gasir.py sociopatterns-infectious_ad.txt 100 30
}

#python plot_histogram <arquivo_resultado> <número de indivíduos do grafo>
python plot_histogram.py sociopatterns-infectious_ad.result 410

exit 0
