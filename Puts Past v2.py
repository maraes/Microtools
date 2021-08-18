import os
import shutil
from unidecode import unidecode as semAcento


def check_dir_fonte(d = None):
	if not d:
		print('Nenhum caminho digitado.')
		exit()
		#os.chdir('.')
	else:
		try:
			os.chdir(d)
		except:
			print('Caminho especificado nao encontrado.')	
		
		
def list_dir(src):
	var = os.listdir(src)
	#print('\n'.join(var))
	
	lista = []
	#print(f'Conteudo deste diretório:::: ***{os.getcwd()}***\n\n\nLISTAGEM:\n\n')
	
	i = 0
	for arquivo in var:
		if arquivo.endswith('.pdf'):
			if i < 10:
				print(f'-0{i} {arquivo}')
				i+=1
				lista.append(arquivo)
			else:
				print(f'-{i} {arquivo}')
				i+=1
				lista.append(arquivo)
					
			
		else:
			if i < 10:
				print(f'-0{i} {arquivo.upper()}' + '(DIR)'.rjust(50 - len(arquivo))    )
				i+=1
			else:
				print(f'-{i} {arquivo.upper()}' + '(DIR)'.rjust(50 - len(arquivo))    )
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
	try:
		list_dir(src)	
		dest = input('Check Pasta Destino: ')
		term = input('Check Termo: ')
		pasta2_pasta_by_termo(src,dest, semAcento(term).lower())
	except:
		print('Caminho nao encontrado.')
		break
