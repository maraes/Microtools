import os
from datetime import datetime


diretorio = '.'
data = ''
termo_procurar = '2021' 

mp4 = '.mp4'
mkv = '.mkv'

tipo_entrada = ''
reconhecimento = '%Y-%m-%d %H-%M-%S'                # '%Y-%m-%d %H-%M-%S'
saida =   '%d-%m-%Y  %H-%M-%S'                 # '%d-%m-%Y  %H-%M-%S'


os.chdir(diretorio)
print(os.getcwd())


for root , dirs , files in os.walk(diretorio):
	for file in files:
		if file.endswith(mp4) or file.endswith(mkv):
			if termo_procurar in file:
				
				tipo_entrada , extensao  = os.path.splitext(file)
				try:
					padrao = datetime.strptime(tipo_entrada,reconhecimento )
				except:
					continue
					print('Padrao nao reconhecido')
					
				data = padrao.strftime(saida)
				
				data = data + extensao
				
				os.rename(file,data)
				
				
				
