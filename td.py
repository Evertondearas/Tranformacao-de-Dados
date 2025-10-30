import os 
import tabula  
import pandas as pd 
import zipfile 

#caminho do arquivo que as tabelas serão extraidas
caminho_arquivo = 'Anexo.pdf'  

tabelas = tabula.read_pdf(caminho_arquivo, pages='3-180', lattice=True) #extraindo tabelas do pdf

#concatenando tabelas 
tabela_completa = pd.concat(tabelas, ignore_index=True)

#alterando nome das colunas
ultima_tabela = tabela_completa.rename(columns={'RN\r(alteração)': 'RN (alteração)', 'OD': 'Seg. Odontologico', 'AMB': 'Seg. Ambulatorial'})

#criando csv
ultima_tabela.to_csv('Anexo.csv', index=False)

csv_nome = 'Anexo.csv'  
zip_nome = 'Teste_Everton.zip'
#zipando arquivo
with zipfile.ZipFile(zip_nome, 'w') as zp:
    zp.write(csv_nome, os.path.basename(csv_nome))