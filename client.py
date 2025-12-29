import os, fcntl, socket, struct, select, sys
from cryptography.fernet import Fernet

# Configurações fixas (Use a mesma KEY no server e client)
KEY = b'Substitua_Pela_Sua_Chave_Gerada_Aqui='
TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000

def setup_tun(name='tun0'):
    try:
        tun = os.open('/dev/net/tun', os.O_RDWR)
        ifr = struct.pack('16sH', name.encode('utf-8'), IFF_TUN | IFF_NO_PI)
        fcntl.ioctl(tun, TUNSETIFF, ifr)
        os.system(f"ip addr add 10.8.0.2/24 dev {name}")
        os.system(f"ip link set dev {name} up")
        return tun
    except Exception as e:
        print(f"Erro ao criar interface: {e}. Rode como SUDO.")
        sys.exit(1)

def start_vpn(server_ip, server_port):
    cipher = Fernet(KEY)
    tun_fd = setup_tun()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = (server_ip, server_port)

    print(f"VPN Cliente rodando. Túnel: 10.8.0.2 -> {server_ip}")

    try:
        while True:
            r, _, _ = select.select([tun_fd, sock], [], [])
            for fd in r:
                if fd == tun_fd:
                    packet = os.read(tun_fd, 1500)
                    sock.sendto(cipher.encrypt(packet), server_addr)
                elif fd == sock:
                    data, _ = sock.recvfrom(4096)
                    os.write(tun_fd, cipher.decrypt(data))
    except KeyboardInterrupt:
        print("\nEncerrando...")
    finally:
        os.close(tun_fd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: sudo python3 client.py <IP_DO_SERVIDOR>")
    else:
        start_vpn(sys.argv[1], 8888)
