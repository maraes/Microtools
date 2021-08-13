import os
import shutil



os.chdir('C:\Livros')
i = 0
for root , dirs , files in os.walk('.'):
	
	for file in files:
		if file.endswith('.pdf'):
			if  '- Desconhecido' in file:
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
