import os
from unidecode import unidecode as semAcentos
from time import sleep
#Programa usado para pesquisar em grande massa de arquivos pdf em um diretorio por padrao no nome


while True:
	list_files = []
	cont = 1
		
	sleep(1)
	os.system('cls')
	url = input('Diretory Input Origin: ')
	if not url == None:
		try:
			os.chdir(url)
		except:
			print('Err Directory no Exists')
			#continue
	else:
		os.chdir('.')
	
	print(f'\nPesquisando em Atual: {os.getcwd()}\n\n')
	pattern = input('Input term searches: ')
	for file in os.listdir():
		if file.endswith('.pdf'):
			if semAcentos(pattern.lower()) in semAcentos(file.lower()):
				#print(f'{cont}: {file}')
				list_files.append(file)
				cont+=1
	
	if not len(list_files):
		print('NENHUM resultado!')
		continue
		
	for index , file in enumerate(list_files):
		print(f'{index}: {file}')
	
	choose = input('\n\nSelecione Valor Correspondente.Ou\n [-1] para Reiniciar: ')
	if choose.isdigit():
		choose = int(choose)
		if choose == -1:
			continue
		else:
			os.system(f'{list_files[choose]}')
				
			
	
	
			
			
			
				
	
	
