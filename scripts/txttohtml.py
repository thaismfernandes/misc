import os
from datetime import datetime

def ler_conteudo_txt(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()

def salvar_conteudo_html(caminho_arquivo, conteudo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo)

def converter_txt_para_html(conteudo_txt):
    linhas = conteudo_txt.split('\n')
    conteudo_html = "<html>\n<head>\n<title>Resumo do Dia</title>\n</head>\n<body>\n"
    conteudo_html += "<h1>Resumo do Dia</h1>\n"
    
    for linha in linhas:
        if linha.strip():
            conteudo_html += f"<p>{linha}</p>\n"
        else:
            conteudo_html += "<br/>\n"

    conteudo_html += "</body>\n</html>"
    return conteudo_html

def main():
    # Caminho para o arquivo de texto a ser convertido
    pasta_newsletters = 'newsletters'
    pasta_resumos = 'resumos'
    caminho_arquivo_txt = os.path.join(pasta_newsletters, 'resumododia.txt')
    
    # Verificar se o arquivo TXT existe
    if not os.path.exists(caminho_arquivo_txt):
        print(f"O arquivo {caminho_arquivo_txt} não foi encontrado.")
        return
    
    # Ler o conteúdo do arquivo de texto
    conteudo_txt = ler_conteudo_txt(caminho_arquivo_txt)
    
    # Converter o conteúdo do texto para HTML
    conteudo_html = converter_txt_para_html(conteudo_txt)
    
    # Criar a pasta de resumos se ela não existir
    if not os.path.exists(pasta_resumos):
        os.makedirs(pasta_resumos)
    
    # Gerar o nome do arquivo HTML com a data atual
    data_atual = datetime.now().strftime("%d%m%y")
    nome_arquivo_html = f'resumo_{data_atual}.html'
    caminho_arquivo_html = os.path.join(pasta_resumos, nome_arquivo_html)
    
    # Salvar o conteúdo HTML
    salvar_conteudo_html(caminho_arquivo_html, conteudo_html)
    print(f"Arquivo HTML salvo em: {caminho_arquivo_html}")

if __name__ == '__main__':
    main()

