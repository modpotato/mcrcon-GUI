import sys, string, os
from colorama import Fore, Style
import ctypes
import time
from os import system

def clear():
  
        _ = system('cls')

def wait5():
    print(Fore.MAGENTA + 'loading')
    time.sleep(1)
    clear()
    print(Fore.MAGENTA + 'loading.')
    time.sleep(1)
    clear()
    print(Fore.MAGENTA + 'loading..')
    time.sleep(1)
    clear()
    print(Fore.MAGENTA + 'loading...')
    time.sleep(1)
    clear()


title = "Unofficial mcrcon GUI by Mod#1337"
ctypes.windll.kernel32.SetConsoleTitleA(title)

print(Fore.BLUE + "Welcome to the unofficial MCRCON Gui")
print(Style.RESET_ALL)
wait5()
clear()

print(Fore.MAGENTA + 'Commands can be executed in succession but no spaces are allowed.')

print(Fore.MAGENTA + 'Things like ' + Fore.RED + 'save-all stop' + Fore.MAGENTA + ' are allowed.')
print(Fore.MAGENTA + 'As well as ' + Fore.RED + '"say 123123"' + Fore.MAGENTA + ' is allowed however,')
print(Fore.RED + 'say 123123' + Fore.MAGENTA + ' is not allowed')
input(Fore.MAGENTA + "Press " + Fore.RED + "Enter " + Fore.MAGENTA + "to continue.")
clear()

hostname = input(Fore.RED + 'Hostname '+ Fore.MAGENTA + '(such as 1.1.1.1)' + Style.RESET_ALL +'\n')
password = input(Fore.RED + 'Password ' + Style.RESET_ALL +'\n')

clear()

print(Fore.MAGENTA + "To close either press Control + C or close the window.")

while True:
    command = input(Fore.RED + "Execute command: ")
    system('mcrcon.exe -H ' + hostname + ' -p ' + password + ' ' + command)