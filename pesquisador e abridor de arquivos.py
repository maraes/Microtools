import os
from unidecode import unidecode as semAcentos


def url(endereco = '.'):
	os.chdir(endereco)
	return endereco




def pesquisar(search):
	lista = []
	i = 0
	for root , dirs , files in os.walk('.'):
		
		for file in files:
			
			if file.endswith('.pdf'):
				
				if search in semAcentos(file.lower()):
					
					print(f'{i}: {file}')
					lista.append(file)
					i += 1
				
	return lista		
end = input('Endereço de procura: ')
try:
	r = url(end)
	print(f'Busca neste pasta: {r}')
except:
	print('Busca na pasta local mesmo')
	url()

while True:
	search = input('\n\nPASTA ATUAL\n\nPESQUISAR: ')
	os.system('cls')
	search = semAcentos(search)
	search = search.lower()
	
	lista = pesquisar(search)
	i = input('\nNúmero correspondente ou[ -1: cancelar]: ')
	try:
		i = int(i)
	except:
		print('\nDigite apenas o valor do item')
		continue
	if i == -1:
		continue
	
	
	try:
		os.system(f'"{lista[i]}"')	
	except:
		print('Entrada invalida!!!!')		
