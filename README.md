# Transformação de Dados 

Este projeto foi feito para automatizar a extração e transformação dos dados da tabela "Rol de Procedimentos e Eventos em Saúde" contida no PDF do Anexo I da ANS. A ideia é pegar todas as páginas do documento, organizar os dados em formato CSV e gerar um `.zip` com o resultado.

## O que o script faz

1. Lê todas as páginas do PDF (de 3 a 180)
2. Extrai as tabelas usando a biblioteca `tabula`
3. Junta tudo em um único DataFrame
4. Renomeia as colunas 
5. Salva o resultado em um arquivo CSV
6. Compacta o CSV em um arquivo chamado `Teste_Everton.zip`

## Como rodar

1. Instale as dependências:
   ```bash
   pip install pandas tabula-py
