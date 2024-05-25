    # O script rodatudo.py executará cada um dos scripts na ordem especificada:
    # Baixa as newsletters.
    # Converte os arquivos HTML para TXT.
    # Gera resumos dos arquivos TXT.
    # Converte o resumo do dia de TXT para HTML.
    # Deleta a pasta newsletters.



import subprocess

def rodar_script(script):
    result = subprocess.run(['python', script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Executou {script} com sucesso.")
    else:
        print(f"Falha ao executar {script}.")
        print(result.stdout)
        print(result.stderr)
        raise Exception(f"Erro ao executar {script}")

def main():
    scripts = [
        'baixarnews.py',
        'htmltotext.py',
        'resumenews.py',
        'txttohtml.py',
	'deletapastanews.py'
    ]
    
    for script in scripts:
        rodar_script(script)

if __name__ == '__main__':
    main()


