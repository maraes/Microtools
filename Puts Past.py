import os
import shutil
from unidecode import unidecode as semAcento


def check_dir_fonte(d = None):
	if not d:
		os.chdir('.')
	else:
		os.chdir(d)
		
		
def list_dir():
	var = os.listdir()
	lista = []
	print(f'Conteudo deste diretório:::: ***{os.getcwd()}***\n\n\nLISTAGEM:\n\n')
	
	i = 0
	for arquivo in var:
		if arquivo.endswith('.pdf'):
			print(f'{i}: {arquivo}')
			lista.append(arquivo)
			i+=1
	print(f"\n**Total de arquivos pdf's : {i-1} arquivos")
	return lista

def pasta2_pasta_by_termo(pasta_origem = None , pasta_destino = None , termo = None):
	
		
	check_dir_fonte(pasta_origem)
	lista_pdf = list_dir()
	
	if not os.path.exists(pasta_destino):
		os.mkdir(pasta_destino)
	for root , dirs , files in os.walk('.'):
	
		if os.getcwd() == pasta_origem:
					
			for file in files:
				if file.endswith('.pdf'):
					if termo in semAcento(file).lower():
						
						origem = os.path.join(root,file)
						destino = os.path.join(f'{pasta_destino}',file)
						
						 
						
						shutil.move(origem , destino)
						
						
							
					
							
			
							
							
							
	print('Done !')		
			
		
		
	
	
	
		


		

src = input('Check Pasta Origem: ')
while True:
		
	dest = input('Check Pasta Destino: ')
	term = input('Check Termo: ')

	pasta2_pasta_by_termo(src,dest, semAcento(term).lower())
