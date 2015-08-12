from termcolor import colored, cprint
import subprocess
import main

def objective():
    subprocess.call('clear')
    cprint("\n\nObjective:", 'green', attrs=['bold'])
    cprint("    Looking for a Python programmer position to refine my skills and to build\n    new ones.", 'green')
    main_menu = raw_input(colored("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHit Enter to return to the Main Menu:\n>>> ", 'green',attrs=['bold']))

    if main_menu == "":
        main.menu()

    else:
        main.menu()
subprocess.call("clear")

