Criar diretório e ambiente virtual

1. **Criação do diretório:**
   Primeiro, crie o diretório onde você deseja armazenar seu projeto:
   ```bash
   mkdir nome_do_diretorio
   cd nome_do_diretorio
   ```

2. **Criação do ambiente virtual:**
   Em seguida, crie um ambiente virtual dentro desse diretório:
   ```bash
   python3 -m venv env
   ```

3. **Ativação do ambiente virtual:**
   Agora, ative o ambiente virtual:
   No Linux ou macOS:
     ```bash
     source env/bin/activate
     ```

Quando o ambiente virtual estiver ativado, você verá o nome do ambiente entre parênteses no início da linha de comando. Isso indica que todos os pacotes que você instalar usando o `pip` serão instalados apenas nesse ambiente virtual, evitando conflitos com outras instalações de Python no sistema.

4. **Deletar diretório:**
   Primeiro, crie o diretório onde você deseja armazenar seu projeto:
   ```bash
   rm -rf file
   ```