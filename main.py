import sys, time
import os
from colorama import Fore, Back, Style
import subprocess
from rich import print
from rich.console import Console


def clear_screen():
    console = Console()
    console.clear()

def print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.5/500)


def main():
    clear_screen()
    print(Fore.GREEN + "╭──────────────────────────────────────────────────────────────────╮")
    print("│      __  __ __  __ ____         │ Created by: " + Fore.RED + "Milis0f" + Fore.GREEN +"            │")
    print("│     / / / // / / // __ )        │                                │")
    print("│    / /_/ // / / // __  │        │                                │")
    print("│   / __  // /_/ // /_/ /         │                                │")
    print("│  /_/ /_/ \____//_____/" + Fore.RED + "v1" + Fore.GREEN +"        │                                │")
    print("│                                 │                                │")
    print("│──────────────────────────────────────────────────────────────────│")
    print("│                                                                 │")
    print("│                                                                  │")
    print("│                                                                  │")
    print("│                                                                  │")
    print("│                                                                  │")
    print("│                                                                  │")
    print("╰──────────────────────────────────────────────────────────────────╯")
    try:
      choice = int(input("Enter Your choice: "))
    except (ValueError, EOFError, KeyboardInterrupt):
      return print('\n[!] Interrupted! or Wrong Value')
   
    if choice not in range(4):
      return('[!] Invalide Choice')
   
    if choice == 1:
      script_a_lancer = "test.py"  # Remplacez par le chemin de votre script
      subprocess.run(["python", script_a_lancer])
      
    elif choice == 2:
      print('''[!] in building...''')
      
    elif choice == 3:
      print('''[!] in building...''')
      
    else:
      print("Invalide choice")
    
    




if __name__ == '__main__':
    main()
