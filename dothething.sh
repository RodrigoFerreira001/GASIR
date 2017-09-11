#$1 gene_size
#$2 file output

for((number = 0; number < 10; number++)){
	#python sir_genetic_algorithm <grafo> <porcentagem_infectados> <número de vacinas> <arquivo resultado>
	python sir_genetic_algorithm.py jazz.txt 0.025 $1 $2
}

#python plot_histogram <arquivo_resultado> <número de indivíduos do grafo>
python plot_histogram.py $2 $3

exit 0
