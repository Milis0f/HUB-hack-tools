import sys
import time
import os
import subprocess
from colorama import Fore
from rich.console import Console


def clear_screen():
    console = Console()
    console.clear()

def slow_print(message: str) -> None:
    for c in message + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5 / 500)


def main():
    clear_screen()
    slow_print(Fore.GREEN + "╭──────────────────────────────────────────────────────────────────╮")
    slow_print(
        "│      __  __ __  __ ____         │ Created by: "
        + Fore.RED
        + "Milis0f"
        + Fore.GREEN
        + "            │"
    )
    slow_print("│     / / / // / / // __ )        │                                │")
    slow_print("│    / /_/ // / / // __  │        │                                │")
    slow_print("│   / __  // /_/ // /_/ /         │                                │")
    slow_print(
        "│  /_/ /_/ \\____//_____/" + Fore.RED + "v1" + Fore.GREEN + "        │                                │"
    )
    slow_print("│                                 │                                │")
    slow_print("│──────────────────────────────────────────────────────────────────│")
    slow_print("│  [1] Network scanner                                              │")
    slow_print("│  [2] Sherlock username search                                     │")
    slow_print("│  [3] Website analyzer                                             │")
    slow_print("│  [4] Port scanner                                                 │")
    slow_print("│  [5] Subdomain finder                                             │")
    slow_print("│  [0] Exit                                                         │")
    slow_print("╰──────────────────────────────────────────────────────────────────╯")
    try:
        choice = int(input("Enter your choice: "))
    except (ValueError, EOFError, KeyboardInterrupt):
        print("\n[!] Interrupted! or Wrong Value")
        return

    if choice == 1:
        subprocess.run(["python", "test.py"])
    elif choice == 2:
        username = input("Enter username: ")
        sherlock_path = os.path.join("tools", "sherlock", "sherlock", "sherlock.py")
        subprocess.run(["python", sherlock_path, username])
    elif choice == 3:
        url = input("Enter URL: ")
        weban_path = os.path.join("tools", "weban", "weban.py")
        subprocess.run(["python", weban_path, url])
    elif choice == 4:
        host = input("Enter host: ")
        port_range = input("Enter port range (start-end): ")
        try:
            start_str, end_str = port_range.split("-", 1)
        except ValueError:
            print("Invalid range format")
            return
        portscan_path = os.path.join("tools", "portscan", "portscan.py")
        subprocess.run(["python", portscan_path, host, start_str, end_str])
    elif choice == 5:
        domain = input("Enter domain: ")
        subfinder_path = os.path.join("tools", "subfinder", "subfinder.py")
        subprocess.run(["python", subfinder_path, domain])
    elif choice == 0:
        print("Goodbye!")
    else:
        print("[!] Invalid choice")
    
    




if __name__ == '__main__':
    main()
