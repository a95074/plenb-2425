# Documentação do Código

## Importação de Módulos

- **json**: Para manipulação de dados JSON.
- **requests**: Para fazer requisições HTTP.
- **BeautifulSoup**: Para analisar o conteúdo HTML.

## Função `get_doenca_info(url)`

- Faz uma requisição HTTP para obter o conteúdo HTML da página de uma doença específica.
- Usa BeautifulSoup para analisar o HTML e extrair informações como data, descrição, fonte, site e nota.
- Retorna um dicionário com essas informações.

## Função `doencas_letra(letra)`

- Faz uma requisição HTTP para obter a lista de doenças que começam com uma letra específica.
- Usa BeautifulSoup para analisar o HTML e extrair o nome e URL de cada doença.
- Chama `get_doenca_info(url)` para obter informações detalhadas sobre cada doença.
- Retorna um dicionário com as informações das doenças.

## Coleta de Informações

- Itera sobre todas as letras do alfabeto (de 'a' a 'z').
- Chama `doencas_letra(letra)` para cada letra e combina os resultados em um único dicionário.

## Salvamento em Arquivo JSON

- Salva o dicionário de doenças em um arquivo JSON chamado "doencas.json".
