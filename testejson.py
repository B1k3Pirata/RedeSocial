import json
with open("./bdados/nivel.json", encoding="utf-8") as meu_json:
	dados = json.load(meu_json)
	for i in dados:
		print(i.medio)
