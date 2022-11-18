from hashTable import HashTable
from ReadFiles import *

from UI import *
import os


class Main():

    # Interface where delivery begins. Package can be viewed at certain times based on user input. After running
    # a delivery simulation, package progress can be viewed based on input time. For example, user can input times 8:35
    # and 9:25 and view package status between those two. Or, after time selection, the user can input [0] to complete
    # delivery. User will not see the address change on package 9 until time >= 10:20

    # 0(1)
    def UserInterface(self):
        print('==============MAIN MENU==============')
        print('IT IS 8:00am.')
        menu = input('Press "Enter" to begin ')

        if menu != None:
            time = input('Enter time in "Military" format \n'
                         'Input: ')
            if (len(time) < 4 or len(time) > 5):
                print('........\nInvalid format, Try again...')
                main = Main()
                main.UserInterface()
                return None

            elif any(c.isalpha() for c in time):
                print('........\nInvalid format, Try again........\n')
                main = Main()
                main.UserInterface()
            ui.run(time)
            ui.PackageStatus(time)
            choice = input('Enter [0] to view complete delivery\n'
                           'Enter [1] to run again\n'
                           'Enter [2] to search package\n'
                           'Enter [3] to exit \n'
                           'Input: ')

            if choice == '0':
                ui.FindAll()

            elif choice == '1':
                main = Main()

                main.UserInterface()

            elif choice == '2':
                print('Searching package at', time)
                option = input('Choose one of the following:\n'
                               'Address  [1]\n'
                               'City     [2]\n'
                               'State    [3]\n'
                               'Zip      [4]\n'
                               'Deadline [5]\n'
                               'Weight   [6]\n'
                               'Status   [7]\n')
                id = input('Enter ID \n'
                           'Input: ')

                ui.FindPackage(option, id, time)
            else:
                SystemExit


main = Main()
main.UserInterface()
