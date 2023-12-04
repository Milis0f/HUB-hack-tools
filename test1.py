import importlib
import subprocess
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.prompt import Prompt, IntPrompt
import ipaddress
import socket
import nmap
import asyncio
from typing import List
from typing_extensions import TypedDict


def clear_screen():
    console = Console()
    console.clear()


def check_modules():
    required_modules = [
        'rich',
        'pyfiglet',
        'ipaddress',
        'nmap'
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


def display_ip_information(ip):
    console = Console()
    table = Table(title=f"Informations pour l'adresse IP : {ip}")
    table.add_column("Propriété", style="cyan", justify="left")
    table.add_column("Valeur", style="green", justify="left")

    table.add_row("Adresse IP", ip)

    try:
        hostname = asyncio.run(get_hostname(ip))
        table.add_row("Nom d'hôte", hostname)
    except Exception as e:
        table.add_row("Nom d'hôte", "N/A")

    try:
        os = asyncio.run(get_os(ip))
        table.add_row("Système d'exploitation", os)
    except Exception as e:
        table.add_row("Système d'exploitation", "N/A")

    console.print(table)


class MenuItem(TypedDict):
    label: str
    action: callable


def menu(items: List[MenuItem], title: str):
    console = Console()
    while True:
        console.print(f"[bold green]{title}[/bold green]\n")
        for index, item in enumerate(items):
            console.print(f"{index + 1}. {item['label']}")

        choice = IntPrompt.ask("\nChoisissez une option (ou 0 pour quitter) :")
        if choice == 0:
            break
        elif 0 < choice <= len(items):
            action = items[choice - 1]["action"]
            action()
        else:
            console.print("[bold red]Option invalide. Veuillez sélectionner une option valide.[/bold red]\n")


def analyze_subnet():
    console = Console()
    ip_network = Prompt.ask("Veuillez saisir l'adresse IP du réseau à analyser (au format CIDR) :")
    try:
        network = ipaddress.ip_network(ip_network)
        addresses = [str(ip) for ip in network.hosts()]
        valid_ips = []

        for address in addresses:
            try:
                asyncio.run(get_hostname(address))
                valid_ips.append((address, "✔️"))
            except:
                valid_ips.append((address, "❌"))

        table = Table(title="Liste des adresses IP dans le réseau")
        table.add_column("Adresse IP", style="cyan", justify="left")
        table.add_column("Valide", style="green", justify="left")

        for ip, status in valid_ips:
            table.add_row(ip, status)

        console.print(table)

        selected_ip = Prompt.ask("Entrez l'adresse IP pour obtenir des informations détaillées (ou 'q' pour revenir) :")
        if selected_ip == 'q':
            clear_screen()
        elif selected_ip in addresses:
            display_ip_information(selected_ip)
        else:
            console.print("[bold red]Adresse IP invalide. Veuillez sélectionner une adresse IP valide.[/bold red]\n")

    except ValueError:
        console.print("[bold red]Format d'adresse IP invalide. Veuillez saisir une adresse IP valide au format CIDR.[/bold red]\n")


def view_all_ips():
    console = Console()
    ip_network = Prompt.ask("Veuillez saisir l'adresse IP du réseau à afficher (au format CIDR) :")
    try:
        network = ipaddress.ip_network(ip_network)
        addresses = [str(ip) for ip in network.hosts()]

        table = Table(title="Toutes les adresses IP dans le réseau")
        table.add_column("Adresse IP", style="cyan", justify="left")

        for ip in addresses:
            table.add_row(ip)

        console.print(table)

        selected_ip = Prompt.ask("Entrez l'adresse IP pour obtenir des informations détaillées (ou 'q' pour revenir) :")
        if selected_ip == 'q':
            clear_screen()
        elif selected_ip in addresses:
            display_ip_information(selected_ip)
        else:
            console.print("[bold red]Adresse IP invalide. Veuillez sélectionner une adresse IP valide.[/bold red]\n")

    except ValueError:
        console.print("[bold red]Format d'adresse IP invalide. Veuillez saisir une adresse IP valide au format CIDR.[/bold red]\n")


def main_menu():
    items = [
        {"label": "Analyser un sous-réseau", "action": analyze_subnet},
        {"label": "Voir toutes les adresses IP", "action": view_all_ips},
        {"label": "Quitter", "action": exit}
    ]
    menu(items, "Network Info")


if __name__ == "__main__":
    check_modules()
    main_menu()
