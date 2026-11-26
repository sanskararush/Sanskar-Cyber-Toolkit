import os
import re
import socket
import hashlib
import base64
import urllib.request

def banner():
    os.system('clear')
    print("\033[1;92m" + "=" * 52)
    print("     SANSKAR CYBER LAB - ALL-IN-ONE TOOLKIT v3.0")
    print("=" * 52 + "\033[0m")

def password_checker():
    print("\n\033[1;36m--- PASSWORD STRENGTH CHECKER ---\033[0m")
    password = input("Password likhein: ")
    score = 0
    tips = []
    if len(password) >= 8: score += 1
    else: tips.append("- Kam se kam 8 characters rakhein")
    if re.search(r"[A-Z]", password): score += 1
    else: tips.append("- Ek Capital letter (A-Z) jodein")
    if re.search(r"[a-z]", password): score += 1
    else: tips.append("- Ek Small letter (a-z) jodein")
    if re.search(r"[0-9]", password): score += 1
    else: tips.append("- Ek Number (0-9) jodein")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    else: tips.append("- Ek Special symbol (@, #, $, !) jodein")

    if score <= 2: print("\nStatus: \033[1;31mWEAK\033[0m")
    elif score <= 4: print("\nStatus: \033[1;33mMEDIUM\033[0m")
    else: print("\nStatus: \033[1;32mSTRONG\033[0m")
    for t in tips: print(t)

def port_scanner():
    print("\n\033[1;36m--- PYTHON PORT SCANNER ---\033[0m")
    target = input("Target domain/IP (jaise scanme.nmap.org): ")
    try:
        target_ip = socket.gethostbyname(target)
    except:
        print("Error: Invalid target ya network issue.")
        return
    print(f"Scanning {target} ({target_ip})...")
    ports = {21:"FTP", 22:"SSH", 25:"SMTP", 53:"DNS", 80:"HTTP", 443:"HTTPS", 3306:"MySQL", 8080:"Proxy"}
    for p, s in ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.2)
        if sock.connect_ex((target_ip, p)) == 0:
            print(f"\033[1;32m[+] Port {p} ({s}) -> OPEN\033[0m")
        sock.close()

def header_scanner():
    print("\n\033[1;36m--- SECURITY HEADER SCANNER ---\033[0m")
    url = input("Website URL (jaise https://nmap.org): ")
    if not url.startswith("http"): url = "https://" + url
    sec_headers = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy"]
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as res:
            print(f"\nScanning {url} (Status: {res.status})")
            for h in sec_headers:
                if h in res.headers: print(f"\033[1;32m[SAFE]    {h}\033[0m")
                else: print(f"\033[1;31m[MISSING] {h}\033[0m")
    except Exception as e:
        print("Error:", e)

def crypto_tool():
    print("\n\033[1;36m--- CRYPTOGRAPHY & HASH GENERATOR ---\033[0m")
    print("a) Text ka MD5, SHA-256 & Base64 banayein")
    print("b) Base64 secret code ko decode karein")
    sub = input("Chunein (a/b): ").lower()
    if sub == 'a':
        text = input("Text ya password likhein: ").encode()
        print(f"\n\033[1;33mMD5    :\033[0m {hashlib.md5(text).hexdigest()}")
        print(f"\033[1;32mSHA-256:\033[0m {hashlib.sha256(text).hexdigest()}")
        print(f"\033[1;36mBase64 :\033[0m {base64.b64encode(text).decode()}")
    elif sub == 'b':
        b64 = input("Base64 code paste karein: ")
        try:
            print(f"\n\033[1;32mDecoded Text:\033[0m {base64.b64decode(b64).decode()}")
        except:
            print("Error: Galat Base64 code hai.")

def dns_lookup():
    print("\n\033[1;36m--- DNS & IP LOOKUP TOOL ---\033[0m")
    domain = input("Website ka naam likhein (jaise scanme.nmap.org): ")
    try:
        ip = socket.gethostbyname(domain)
        print(f"\n\033[1;32m[+] {domain} ka IP Address:\033[0m {ip}")
    except:
        print("Error: Domain nahi mila.")

while True:
    banner()
    print("1. Password Strength Checker")
    print("2. Network Port Scanner")
    print("3. Website Security Header Scanner")
    print("4. Cryptography & Hash Generator")
    print("5. DNS & IP Lookup Tool")
    print("0. Exit Toolkit")
    choice = input("\nApna option chunein (0-5): ")

    if choice == '1': password_checker()
    elif choice == '2': port_scanner()
    elif choice == '3': header_scanner()
    elif choice == '4': crypto_tool()
    elif choice == '5': dns_lookup()
    elif choice == '0':
        print("\nExiting Sanskar Cyber Toolkit v3.0. Stay Ethical!")
        break
    else:
        print("\nGalat option! 0 se 5 ke beech number dalein.")
    input("\nMenu par wapas jaane ke liye Enter dabayein...")
