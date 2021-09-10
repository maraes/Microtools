import sys
import os
import shutil

d= input('input diretorio: ')
tipo = ''
suprima = ''
try:
	os.chdir(d)
except:
	sys.exit()
	i = 0
for contents in os.listdir():
	
	if os.path.isfile(contents):
		file = contents
		if file.endswith(tipo):
			if  suprima in file:
				cont+=1
				file , ex = os.path.splitext(file)
				arq = file[:-len(' - Desconhecido')]
				file = file + '.pdf'
				arq = arq + '.pdf'
				
				origem = os.path.join(root , file)
				destino = os.path.join(root,arq)
								
				print(f'*Renomeando de : {file}')
				print(f'**Novo Nome: {arq}')
				
				print(f'Origem: {origem}')
				print(f'Destino:{destino} ')
				
				os.rename(origem , destino)		

print('Done')
print(f'{i} arquivos alterados.')			
