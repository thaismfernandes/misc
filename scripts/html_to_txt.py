from bs4 import BeautifulSoup
import os

# Diretório onde as newsletters HTML estão salvas
newsletters_dir = 'newsletters'

# Processar cada arquivo HTML na pasta newsletters
for idx, filename in enumerate(os.listdir(newsletters_dir), start=1):
    # Ignorar arquivos irrelevantes como .DS_Store
    if filename.startswith('.') or not filename.endswith('.html'):
        print(f"Ignorando arquivo irrelevante {filename}")
        continue
    
    file_path = os.path.join(newsletters_dir, filename)
    
    # Ler o conteúdo do arquivo HTML
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        print(f"Erro de codificação no arquivo {filename}. Ignorando este arquivo.")
        continue
    
    # Converter HTML para texto
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()
    
    # Verificar se o texto não está vazio
    if len(text.strip()) == 0:
        print(f"Arquivo {filename} está vazio. Ignorando.")
        continue
    
    # Nome do arquivo de texto
    text_filename = filename.replace('.html', '.txt')
    text_path = os.path.join(newsletters_dir, text_filename)
    
    # Salvar o texto em um arquivo de texto
    with open(text_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)
    print(f'Texto do arquivo {filename} salvo em {text_path}.')

print("Processamento concluído.")

