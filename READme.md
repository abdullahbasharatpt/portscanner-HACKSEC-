# Port Scanner - HACKSEC 🔍

This is a simple Python-based **Port Scanner** built as part of my cybersecurity internship with HACKSEC.

It scans for open TCP ports on a given IP address and port range, handles invalid inputs, and displays open ports in a clean output format.

---

## 🛠 Features
- Scan custom IP addresses and port ranges
- Shows open ports
- Handles invalid IP or port range input gracefully
- Lightweight and fast using `socket` module

---

## 💻 Usage

```bash
# Run the script
python portscanner.py

# Example input:
Enter IP address to scan: 127.0.0.1
Enter starting port: 20
Enter ending port: 100
