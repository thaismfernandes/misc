import os
import shutil

def deletar_pasta(pasta):
    if os.path.exists(pasta):
        shutil.rmtree(pasta)
        print(f"A pasta '{pasta}' e seu conteúdo foram deletados.")
    else:
        print(f"A pasta '{pasta}' não foi encontrada.")

def main():
    pasta_newsletters = 'newsletters'
    deletar_pasta(pasta_newsletters)

if __name__ == '__main__':
    main()

