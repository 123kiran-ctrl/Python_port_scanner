import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target} from port {start_port} to {end_port}\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN]   Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    scan_ports(target, start_port, end_port)


