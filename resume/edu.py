from termcolor import colored, cprint
import subprocess
import main

def edu():
    subprocess.call("clear")
    cprint ("\n\n\nEducation:", 'green', attrs=['bold'])
    cprint ("   Self-educated from online recorces and books. Such recorces include\n   linuxacademy.com, puralsight.com, and books like Learn Python The \n   Hard Way.", 'green')


    main_menu = raw_input(colored("\n\n\n\n\n\n\n\n\n\n\n\n\nHit Enter to return to Main Menu:\n>>> ", 'green', attrs=['bold']))
    
    if main_menu == "":
        main.menu()
    else:
        main.menu()    


subprocess.call("clear")
