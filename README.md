# Simple Python VPN (Layer 3)

Este é um projeto didático de uma VPN de camada 3 escrita em Python, utilizando interfaces **TUN/TAP** e criptografia simétrica.

## 🚀 Funcionalidades
- Criação dinâmica de túnel virtual (TUN).
- Criptografia de pacotes usando a biblioteca `cryptography` (Fernet).
- Comunicação via socket UDP para alta performance.

## 📋 Pré-requisitos
- Linux (necessário para interfaces TUN/TAP).
- Python 3.x.
- Acesso root (sudo).

## 🔧 Instalação
1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/my-python-vpn.git](https://github.com/SEU_USUARIO/my-python-vpn.git)
   cd my-python-vpn
Instale as dependências:

Bash

pip install -r requirements.txt
🛠️ Configuração Inicial
Gere uma chave de criptografia para que o cliente e o servidor possam conversar:

Python

python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"
Importante: Copie a chave gerada e substitua a variável KEY tanto no client.py quanto no server.py.

💻 Como Usar
1. No Servidor (VPS):
Habilite o redirecionamento de pacotes e rode o servidor:

Bash

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo python3 server.py
2. No Cliente:
Inicie a conexão apontando para o IP do seu servidor:

Bash

sudo python3 client.py <IP_DO_SERVIDOR>
Aviso: Este projeto tem fins educacionais. Não substitui VPNs comerciais de alta segurança.
