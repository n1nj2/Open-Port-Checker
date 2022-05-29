from socket import socket
from pyfiglet import Figlet
import pyfiglet
from colorama import init, Fore, Back, Style
import socket
import concurrent.futures
from datetime import datetime
import threading
from os import system, name

def clear():
  
    # Windows
    if name == 'nt':
        _ = system('cls')
  
    # Mac & Linux
    else:
        _ = system('clear')
clear()

print(Fore.GREEN + "\n")

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print(Fore.WHITE + "Made by Clxpz#5854")
print('\n')
print(Fore.RED + "This scans every Port from 1-65535")
print('\n')

print_lock = threading.Lock()

ip = input(Fore.LIGHTBLUE_EX + "Enter the IP to scan: ")

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.WHITE + f"[{port}]" + Fore.GREEN + " Opened")
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(65535):
        executor.submit(scan, ip, port + 1)