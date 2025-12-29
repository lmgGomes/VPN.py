# Simple Python VPN (Layer 3)

Este é um projeto didático de uma VPN de camada 3 escrita em Python, utilizando interfaces **TUN/TAP** e criptografia simétrica.

## 🚀 Funcionalidades
- Criação dinâmica de túnel virtual (TUN).
- Criptografia de pacotes usando a biblioteca `cryptography`.
- Comunicação via socket UDP.

## 📋 Pré-requisitos
- Linux (Ubuntu, Debian, etc).
- Python 3.x.
- Acesso root (sudo).

## 🔧 Instalação

1. Clonar o repositório:
```bash
git clone https://github.com/lmgGomes/VPN.py.git
cd VPN.py
Instale as dependências:

Bash

pip install cryptography
🛠️ Configuração Inicial
Gere uma chave de criptografia para que o cliente e o servidor possam conversar:

Bash

python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"
Importante: Copie a chave gerada no terminal e cole na variável KEY dentro do client.py e do server.py.

💻 Como Usar
1. No Servidor (VPS)
Habilite o roteamento de pacotes e rode o servidor:

Bash

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo python3 server.py
2. No Cliente
Inicie a conexão apontando para o IP do seu servidor:

Bash

sudo python3 client.py <IP_DO_SERVIDOR>
Aviso: Este projeto tem fins educacionais. Não substitua VPNs comerciais de alta segurança.


---

### O que foi corrigido:
1.  **Blocos de Código:** Agora todos os comandos estão dentro de ` ```bash ` e ` ``` `, o que cria a caixa de código no GitHub.
2.  **Identação:** Removi o texto "Bash" que estava sobrando e organizei os tópicos.
3.  **Link do Git:** Já deixei o link do seu repositório (`lmgGomes/VPN.py`) no comando de clone.

**Deseja que eu crie um arquivo `.gitignore` para o seu projeto?** Isso serve para evitar que arquivos desnecessários (como pastas temporárias do Python) subam para o seu GitHub.
