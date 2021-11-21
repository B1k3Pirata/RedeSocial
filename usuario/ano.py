import pandas as pd
import csv

#abrindo arquivo
def anos():
	arq= open('anos.csv', encoding='utf-8',delimiter="\n")
	r = csv.writer(arq)
	for i in range(1920+1, 2030):
		#r.writerow([i])
		return(i)
 anos   

#gravando
