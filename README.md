# Simple Python VPN (Layer 3)

Este é um projeto didático de uma VPN de camada 3 escrita em Python, utilizando interfaces **TUN/TAP** e criptografia simétrica.

## 🚀 Funcionalidades
* Criação dinâmica de túnel virtual (TUN).
* Criptografia de pacotes usando a biblioteca `cryptography`.
* Comunicação via socket UDP para alta performance.

## 📋 Pré-requisitos
* Linux (Ubuntu, Debian, etc).
* Python 3.x.
* Acesso root (sudo).

## 🔧 Instalação

1. Clonar o repositório:
```bash
git clone https://github.com/lmgGomes/VPN.py.git
cd VPN.py```

Instale as dependências:

```Bash
pip install cryptography```

🛠️ Configuração Inicial
Gere uma chave de criptografia para que o cliente e o servidor possam conversar:

Bash

python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key())"
Importante: Copie a chave gerada no seu terminal e cole-a na variável KEY dentro do arquivo client.py e do arquivo server.py.

💻 Como Usar
1. No Servidor (VPS)
Habilite o roteamento de pacotes e rode o servidor:

Bash

sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo python3 server.py
2. No Cliente
Inicie a conexão apontando para o IP público do seu servidor:

Bash

sudo python3 client.py <IP_DO_SERVIDOR>
Aviso: Este projeto tem fins educacionais. Não substitua VPNs comerciais de alta segurança.


---


**Dica Extra:** Se você quiser que o seu projeto apareça para mais pessoas no GitHub, você pode adicionar "Tags" (topics) no repositório como `python`, `vpn`, `networking` e `security`.

Quer que eu te ajude a criar o arquivo `requirements.txt` para que as pessoas possam instalar tudo com um único comando?
