import sys, time
import os
from rich import print

def print(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./500)


print("Hello, [bold magenta]World[/bold magenta]!")
def main():
    print("╭──────────────────────────────────────────────────────────────────╮")
    print("│      __  __ __  __ ____         │ Created by: Milis0f            │")
    print("│     / / / // / / // __ )        │                                │")
    print("│    / /_/ // / / // __  │        │                                │")
    print("│   / __  // /_/ // /_/ /         │                                │")
    print("│  /_/ /_/ \____//_____/ v1       │                                │")
    print("│                                 │                                │")
    print("│──────────────────────────────────────────────────────────────────│")
    print("│                                                                  │")
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
      os.system('clear')
      os.system('bash -c "python3 /tools/tools.py"')
      
    elif choice == 2:
      print('''[!] in building...''')
      
    elif choice == 3:
      print('''[!] in building...''')
      
    else:
      print("Invalide choice")
    
    




if __name__ == '__main__':
    main()
