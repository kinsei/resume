from termcolor import colored, cprint
import main
import more
import subprocess

def history():

    cl = subprocess.call("clear")
    cprint ("\nWork History:", 'green', attrs=['bold'])
    cprint ("    Your looking at. This is a project to highlight some of my abilities. I\n    also have more projects that can be seen on git hub at\n    https://github.com/kinsei/", 'green')
    
    main_menu = raw_input(colored("\n\n\n\n\n\n\n\n\n\n\n\n\n\nWould you like to see more? (y/n):\n\n>>> ", 'green', attrs=['bold']))

    if main_menu == "n":
        cl
        main.menu()
    elif main_menu == "no":
        cl
        main.menu()
    elif main_menu == "No":
        cl
        main.menu()
    elif main_menu == "y":
        cl
        more.more()
    elif main_menu == "yes":
        cl
        more.more()
    elif main_menu == "Yes":
        cl
        more.more()
        
    else:
        cl
        main.menu()


subprocess.call("clear")
