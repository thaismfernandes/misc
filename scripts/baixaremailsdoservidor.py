import imapclient
import email
from email.header import decode_header
from bs4 import BeautifulSoup
import os

# Configurar conexão com o servidor de email
def conectar_servidor_email():
    server = imapclient.IMAPClient('outlook.office365.com', ssl=True)
    server.login('email', 'senha')
    return server

# Selecionar a caixa de entrada
def selecionar_caixa_entrada(server):
    server.select_folder('INBOX')

# Buscar emails com o assunto 'Teste'
def buscar_emails(server, assunto='Teste'):
    return server.search(['SUBJECT', assunto])

# Criar pasta para armazenar as newsletters, se não existir
def criar_pasta_newsletters(pasta='newsletters'):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

# Processar cada email encontrado e salvar em html
def salvar_email_html(body, idx, pasta='newsletters'):
    soup = BeautifulSoup(body, "html.parser")
    html_filename = os.path.join(pasta, f'newsletter_{idx}.html')
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    print(f'Email salvo como HTML: {html_filename}')

def salvar_email_texto(body, idx, pasta='newsletters'):
    text_filename = os.path.join(pasta, f'newsletter_{idx}.txt')
    with open(text_filename, 'w', encoding='utf-8') as f:
        f.write(body.decode())
    print(f'Email salvo como texto: {text_filename}')

def processar_emails(server, mensagens, pasta='newsletters'):
    for idx, uid in enumerate(mensagens, start=1):
        raw_message = server.fetch([uid], ['BODY[]', 'FLAGS'])
        msg = email.message_from_bytes(raw_message[uid][b'BODY[]'])
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/html":
                    body = part.get_payload(decode=True)
                    salvar_email_html(body, idx, pasta)
        else:
            body = msg.get_payload(decode=True)
            salvar_email_texto(body, idx, pasta)

def main():
    server = conectar_servidor_email()
    selecionar_caixa_entrada(server)
    mensagens = buscar_emails(server)
    criar_pasta_newsletters()
    processar_emails(server, mensagens)
    print("Download concluído.")

if __name__ == '__main__':
    main()

