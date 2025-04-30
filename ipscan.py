import socket
import sys

def port_scan(target_ip, start_port, end_port):
    print(f"Scanning {target_ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)
            s.close()
        except KeyboardInterrupt:
            print("\n[!] Scan cancelled by user.")
            sys.exit()
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            sys.exit()
        except socket.error:
            print("[!] Could not connect to server.")
            sys.exit()

    if not open_ports:
        print("[-] No open ports found in the given range.")

# ----------- Input Handling -------------
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

try:
    target = input("Enter IP address to scan: ").strip()
    if not is_valid_ip(target):
        raise ValueError("Invalid IP address format.")

    start = int(input("Enter starting port: "))
    end = int(input("Enter ending port: "))

    if start < 0 or end > 65535 or start > end:
        raise ValueError("Invalid port range. Ports must be 0–65535 and start ≤ end.")

    port_scan(target, start, end)

except ValueError as ve:
    print(f"[!] Error: {ve}")
except Exception as e:
    print(f"[!] Unexpected error: {e}")
