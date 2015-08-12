


import platform
from termcolor import colored
import os
import intro
import main
import subprocess
opsys = platform.system()

# If OS is Windows inform user of limitation
if opsys == 'Windows':
    
    print colored("This was written for Unix based opperating systems, however it will still workon Windows.", 'red')
    print colored("You will miss some of the functionality. Running this on Linux will give you best results.", 'green')


#########################
## This is the welcome ##
#########################


intro.intro()
main.menu()
subprocess.call("clear")
