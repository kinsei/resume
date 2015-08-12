import time
from termcolor import colored
import subprocess
import ascii


def intro():
    subprocess.call("clear")
    ascii.hello()
    time.sleep(1)
    subprocess.call("clear")
    ascii.And()
    time.sleep(1)
    subprocess.call("clear")
    ascii.welcome()
    time.sleep(1)
    subprocess.call("clear")


subprocess.call("clear")
