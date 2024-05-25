import os
from openai import OpenAI

# Configure seu cliente OpenAI com a chave da API
client = OpenAI(
    api_key= "OPENAIAPIKEY",
)

def ler_conteudo_txt(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()

def salvar_conteudo(caminho_arquivo, conteudo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo)

def gerar_resumo(conteudo, prompt="Resuma o seguinte conteúdo em tópicos, com o título de qual newsletter se refere:\n\n"):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{prompt}{conteudo}",
            }
        ],
        model="gpt-3.5-turbo",
    )
    return response.choices[0].message.content

def processar_arquivo(caminho_arquivo_txt):
    # Ler o conteúdo do arquivo de texto
    conteudo = ler_conteudo_txt(caminho_arquivo_txt)
    
    # Gerar resumo
    resumo = gerar_resumo(conteudo)
    
    return resumo

def main():
    # Caminho para a pasta de textos
    pasta_newsletters = 'newsletters'
    resumos = []

    # Processar cada arquivo na pasta
    for nome_arquivo in os.listdir(pasta_newsletters):
        if nome_arquivo.endswith('.txt'):
            caminho_arquivo_txt = os.path.join(pasta_newsletters, nome_arquivo)
            resumo = processar_arquivo(caminho_arquivo_txt)
            resumos.append(f"Resumo da {nome_arquivo}:\n{resumo}\n\n")
    
    # Gerar resumo geral dos resumos
    resumos_concatenados = "\n".join(resumos)
    resumo_geral = gerar_resumo(resumos_concatenados, prompt="Crie um resumo geral dos seguintes resumos, removendo temas similares:\n\n")
    
    # Criar o conteúdo final do arquivo
    conteudo_final = f"Resumo Geral:\n{resumo_geral}\n\n{resumos_concatenados}"
    
    # Salvar todos os resumos em um único arquivo
    caminho_resumo_final = os.path.join(pasta_newsletters, 'resumododia.txt')
    salvar_conteudo(caminho_resumo_final, conteudo_final)
    print(f"Resumo do dia salvo em: {caminho_resumo_final}")

if __name__ == '__main__':
    main()

