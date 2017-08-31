#$1 gene_size
#$2 file output

for((number = 0; number < 10; number++)){
	python sir_genetic_algorithm.py graph.txt infecteds.txt $1 $2
}

python plot_histogram.py $2 $3

exit 0
