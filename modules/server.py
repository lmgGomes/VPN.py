import os, fcntl, socket, struct, select, sys
from cryptography.fernet import Fernet

KEY = b'Substitua_Pela_Sua_Chave_Gerada_Aqui='
TUNSETIFF = 0x400454ca
IFF_TUN = 0x0001
IFF_NO_PI = 0x1000

def setup_tun(name='tun0'):
    tun = os.open('/dev/net/tun', os.O_RDWR)
    ifr = struct.pack('16sH', name.encode('utf-8'), IFF_TUN | IFF_NO_PI)
    fcntl.ioctl(tun, TUNSETIFF, ifr)
    os.system(f"ip addr add 10.8.0.1/24 dev {name}")
    os.system(f"ip link set dev {name} up")
    return tun

def start_server(port=8888):
    cipher = Fernet(KEY)
    tun_fd = setup_tun()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))
    
    print(f"Servidor VPN escutando na porta {port}...")
    client_addr = None

    while True:
        r, _, _ = select.select([tun_fd, sock], [], [])
        for fd in r:
            if fd == sock:
                data, addr = sock.recvfrom(4096)
                client_addr = addr
                try:
                    os.write(tun_fd, cipher.decrypt(data))
                except: continue
            elif fd == tun_fd:
                if client_addr:
                    packet = os.read(tun_fd, 1500)
                    sock.sendto(cipher.encrypt(packet), client_addr)

if __name__ == "__main__":
    start_server()
