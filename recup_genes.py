import os
import sys
import argparse


# def get_arguments() :
# 	parser = argparse.ArgumentParser(description = '')

# 	parser.add_argument('-i', '-input file', dest = 'gene_list', type = str, required = True, 
# 					help = "list of genes")

# 	parser.add_argument('-i', '-input file 1', dest = 'core_gene_list', type = str, required = True, 
# 	 				help = "list of complementary genes")

# 	 parser.add_argument('-k', '-input file 2', dest = 'accessory_gene_list', type = str, required = True, 
# 	 				help = "list of accessory genes")

# 	args = parser.parse_args()

# 	return args
	

def get_genes(file) :
	genes = []
	with open(file, "r") as filin :
		for line in filin :	
			words = line.split()
			genes.append(words[0][:-1])

	return genes




def main() :

	path_data = "/Users/rgoulanc/Desktop/Rebecca/FAC/M2BI/projet_long/data_projet_long_marqueur/new_marqueur_ok/roary_output_marqueur_ok/_1636985554_all/query_pangenome/"
	path_data_intersection = "/Users/rgoulanc/Desktop/Rebecca/FAC/M2BI/projet_long/data_projet_long_marqueur/new_marqueur_ok/roary_output_marqueur_ok/_1636985554_all/query_pangenome/pan_genome_results_intersection"
	path_data_complement = "/Users/rgoulanc/Desktop/Rebecca/FAC/M2BI/projet_long/data_projet_long_marqueur/new_marqueur_ok/roary_output_marqueur_ok/_1636985554_all/query_pangenome/pan_genome_results_complement"

	#args = get_arguments()
	core_genes = get_genes(path_data_intersection)

	with open(path_data+"/core_genes.txt", "w") as filout :
		for gene in core_genes :
			filout.write("{}\n".format(gene))

	accessory_genes = get_genes(path_data_complement)

	with open(path_data+"/accessory_genes.txt", "w") as filout :
		for gene in accessory_genes :
			filout.write("{}\n".format(gene))

	#print("--------CORE GENES--------\n", core_gene)
	#print("--------ACCESSORY GENES---------\n", accessory_gene)



if __name__ == "__main__" :
	main()


