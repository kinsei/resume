###########################
## This is the main menu ##
###########################

from termcolor import colored, cprint
import time
import subprocess
import ascii
import objective
import edu
import work


def menu():
        
    ascii.main()
    print "\n"
    cprint ("Select from the following:", 'magenta', attrs=['bold'])
    cprint ("\n   1) Objective", 'magenta')
    cprint ("   2) Education", 'magenta')
    cprint ("   3) Work History", 'magenta')
    cprint ("   4) Exit", 'magenta')
    global select
    select = raw_input(colored(">>> ", 'magenta'))
    
    choice()


def choice():

    if select == '1':
        objective.objective()


    elif select == "Objective":
        objective.objective()


    elif select == "objective":
        objective.objective()

    
    elif select == '2':
        edu.edu()


    elif select == "Education":
        edu.edu()


    elif select == "education":
        edu.edu()


    elif select == '3':
        work.history()

    
    elif select == "Work History":
        work.history()


    elif select == "work history":
        work.history()

    elif select == "4":
        subprocess.call("clear")
        exit(0)

    elif select == "Exit":
        exit(0)

    elif select == "exit":
        exit(0)
    

    else:
        cprint ("Invalid selection:", 'red', attrs=['reverse', 'bold'])
        time.sleep(1)
        subprocess.call("clear")
        menu()
subprocess.call("clear")
# comment out the following line 
# before putting into production
# it is for testing only
#menu()
