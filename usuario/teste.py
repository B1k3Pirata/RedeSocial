import csv

arq= open('anos.csv','w',  encoding='utf-8')
r = csv.writer(arq)
for i in range(1920+1, 2030):
    r.writerow([i])
arq.close()
