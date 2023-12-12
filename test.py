

import importlib
import subprocess
from pyfiglet import Figlet
from questionary import select, text
import requests
import socket
import time
import nmap
from scapy.all import ARP, Ether, srp
from rich.console import Console
from rich.progress import Progress
from rich.prompt import Prompt, IntPrompt
from rich.table import Table
from rich.text import Text
from rich import print
from colorama import Fore, Style
import asyncio

def clear_screen():
    console = Console()
    console.clear()

def check_modules():
    required_modules = [
        'scapy',
        'nmap',
        'rich',
        'pyfiglet',
        'questionary',
        'colorama'
    ]

    missing_modules = []

    for module in required_modules:
        try:
            importlib.import_module(module)
        except ImportError:
            missing_modules.append(module)

    if missing_modules:
        print(f"Les modules suivants sont manquants : {', '.join(missing_modules)}")
        install_modules = input("Voulez-vous les installer automatiquement ? (y/n): ")
        if install_modules.lower() == 'y':
            subprocess.check_call(['pip', 'install'] + missing_modules)
        else:
            print("Veuillez installer les modules manquants avant d'exécuter l'application.")
        exit()

async def scan_network(ip_reseau):
    devices = await scan_reseau(ip_reseau)
    console = Console()

    if not devices:
        console.print("[bold red]Aucun appareil actif n'a été trouvé sur le réseau.[/bold red]\n")
        return
    
    table = Table(title="Appareils actifs sur le réseau")
    table.add_column("IP", style="cyan", justify="left")
    table.add_column("MAC", style="green", justify="left")
    table.add_column("Système d'exploitation", style="magenta", justify="left")
    table.add_column("Nom d'hôte", style="yellow", justify="left")

    for device in devices:
        ip = device['ip']
        mac = device['mac']
        os = await get_os(ip)
        hostname = await get_hostname(ip)

        table.add_row(ip, mac, os, hostname)

    console.print(table)

    while True:
        choix = console.input("\nEntrez l'adresse IP pour obtenir un descriptif détaillé (ou 'q' pour quitter) : ")

        if choix == "q":
            break

        found = False
        for device in devices:
            if device['ip'] == choix:
                found = True
                break

        if not found:
            console.print("[bold red]Adresse IP invalide. Veuillez sélectionner une adresse IP valide.[/bold red]\n")
            continue

        console.print("\n[bold cyan]Descriptif complet pour l'adresse IP :[/bold cyan]")
        console.print(f"[bold]IP :[/bold] {device['ip']}")
        console.print(f"[bold]MAC :[/bold] {device['mac']}")
        console.print(f"[bold]Système d'exploitation :[/bold] {await get_os(device['ip'])}")
        console.print(f"[bold]Nom d'hôte :[/bold] {await get_hostname(device['ip'])}")

async def scan_reseau(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=0)[0]

    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices

async def get_os(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-O')
    if ip in scanner.all_hosts():
        if 'osmatch' in scanner[ip] and scanner[ip]['osmatch']:
            return scanner[ip]['osmatch'][0]['name']
    return 'N/A'

async def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except Exception:
        return 'N/A'

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        data = response.json()
        return data['ip']
    else:
        return 'N/A'

def main_menu():
    clear_screen()
    f = Figlet(font='slant')
    title_text = Text(f.renderText("Network Info"))
    title_text.stylize("bold green")

    console = Console()
    console.print(f"{title_text}")
    print("Milis0f\n")

    while True:
        choice = select(
            "Que voulez-vous faire ?",
            choices=[
                "Analyse automatique du réseau",
                "Saisir manuellement l'adresse IP du réseau",
                "Quitter"
            ]
        ).ask()

        if choice == "Analyse automatique du réseau":
            with console.status("[bold cyan]Analyse en cours...", spinner="bouncingBar"):
                asyncio.run(scan_network("192.168.69.1/24"))
            clear_screen()
        elif choice == "Saisir manuellement l'adresse IP du réseau":
            ip_network = text("Veuillez saisir l'adresse IP du réseau à analyser (au format CIDR) :").ask()
            with console.status("[bold cyan]Analyse en cours...", spinner="bouncingBar"):
                asyncio.run(scan_network(ip_network))
            clear_screen()
        elif choice == "Quitter":
            console.print("Merci d'avoir utilisé Network Info. À bientôt !")
            break

if __name__ == "__main__":
    check_modules()
    main_menu()
