from termcolor import colored, cprint
import main
import subprocess as sub


def more():

    sub.call("clear")
    cprint ("Below is a list of GitHub repositories if you would like to download one enter", 'green')
    cprint ("the name of the repo as shown or just press inter to exit:", 'green')
    cprint ("\n\n\n1) Learn-Python-The-Hard-Way:", 'green', attrs=['bold'])
    cprint ("    This repo is, at this time, most of the exercises from the book 'Learn\n    Python The Hard way'. I found this book to be of great use.", 'green')
    cprint ("\n2) Pluralsight:", 'green', attrs=['bold'])
    cprint ("    This repo is a project I did to learn PyQt and how to build GUI's. Its\n    its called Pluarlsight because its a great websight that teaches differant programming languages and this is where I learned PyQt.", 'green')
    cprint ("\n3) Random:", 'green', attrs=['bold'])
    cprint ("    This holds random code like a port scaner and a copy of my .bashrc.", 'green')
    cprint ("\n\n\n\nGit is required for the download to work:", 'green', 'on_red',attrs=['bold'])
    responce = raw_input(colored(">>> "))

    if responce == "":
        main.menu()

    elif responce == "Learn-Python-The-Hard-Way":
        sub.call(['git', 'clone', 'https://github/kinsei/Learn-Python-The-Hard-Way'])
        more()
     
    elif responce == "Pluralsight":
        sub.call(['git', 'clone', 'https://github.com/kinsei/Pluralsight'])
        more()

    elif responce == "Random":
        sub.call(['git', 'clone', 'https://github.com/kinsei/Random'])
        more()


    else:
        main.menu()

sub.call("clear")
