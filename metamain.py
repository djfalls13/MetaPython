#!/usr/bin/env python3

import os


def clearscreen():                                      # Clearscreen Function
    os.system('cls' if os.name == 'nt' else 'clear')

def metatitleshort():
    print("\033[1;32;40m  ")  # Sets Text color to bright green
    print('''


                         ___ ___    ___ ______   ____         ____  __ __  ______  __ __   ___   ____
                        |   |   |  /  _]      | /    |       |    \|  |  ||      ||  |  | /   \ |    \.
                        | _   _ | /  [_|      ||  o  | _____ |  o  )  |  ||      ||  |  ||     ||  _  |
                        |  \_/  ||    _]_|  |_||     ||     ||   _/|  ~  ||_|  |_||  _  ||  O  ||  |  |
                        |   |   ||   [_  |  |  |  _  ||_____||  |  |___, |  |  |  |  |  ||     ||  |  |
                        |   |   ||     | |  |  |  |  |       |  |  |     |  |  |  |  |  ||     ||  |  |
                        |___|___||_____| |__|  |__|__|       |__|  |____/   |__|  |__|__| \___/ |__|__|

                    --------------------------------------------------------------------------------------
                                        A Python Syntax Reference Framework
                                                    Dan Falls
                                                        ''')
    print("\033[1;37;40m ")  # Return to default text


def metatitle():                                        #Function holding Main Title and Description
    print("\033[1;32;40m  ")  # Sets Text color to bright green

    print('''

                         ___ ___    ___ ______   ____         ____  __ __  ______  __ __   ___   ____
                        |   |   |  /  _]      | /    |       |    \|  |  ||      ||  |  | /   \ |    \.
                        | _   _ | /  [_|      ||  o  | _____ |  o  )  |  ||      ||  |  ||     ||  _  |
                        |  \_/  ||    _]_|  |_||     ||     ||   _/|  ~  ||_|  |_||  _  ||  O  ||  |  |
                        |   |   ||   [_  |  |  |  _  ||_____||  |  |___, |  |  |  |  |  ||     ||  |  |
                        |   |   ||     | |  |  |  |  |       |  |  |     |  |  |  |  |  ||     ||  |  |
                        |___|___||_____| |__|  |__|__|       |__|  |____/   |__|  |__|__| \___/ |__|__|

                    --------------------------------------------------------------------------------------
                                        A Python Syntax Reference Framework
                                                    Dan Falls

                                    Additional Credit and thanks to:
                       Derak Banas: Python in One Video https://youtu.be/N4mEzFDjqtA
                                                        and
                Chris Hawkes: Python 3.5 https://youtu.be/c15ZvFsC9Hw?list=PLei96ZX_m9sW2Ih2W_MVi0kMscY3CfCpG
                _____________________________________________________________________________________________''')

    desctuple =  ('This is a Python3 program about... Python.',
                  'The goal is to make this a simple but quick useful Syntax Reference',
                   'program for the Python 3 language.',
                   '*Note: This program is built for Linux and will load text content in Nano to take advantage color coding.')

    print(desctuple[0].center(120))
    print(desctuple[1].center(120))
    print(desctuple[2].center(120))
    print("\033[1;37;40m ")  # Return to default text

    #print(desctuple[3].center(100),'\n')



# Beginning of program

clearscreen()
metatitle()


try:
    input("Press Enter to continue")  # Cheat to pause program
except SyntaxError:
    pass




while True:



    while True:
        clearscreen()  # Starts Loop with Clear Screen

        metatitleshort()  # Loads Title minus credits


        readlistfile = open('notes/list_categories_.txt')  # Loads Categories List
        print(readlistfile.read())
        readlistfile.close()

        print("\033[1;32;40m  ")  # Sets Text color to bright green
        x = input('                 Enter a number:  ')  # Accepts User Input
        print("\033[1;37;40m \n")  # Return to default text



        if x == '1':
            clearscreen()
            metatitleshort()

            readfile = open('notes/19.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '2':
            clearscreen()
            metatitleshort()

            readfile = open('notes/20.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '3':
            clearscreen()
            metatitleshort()

            readfile = open('notes/30.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '4':
            clearscreen()
            metatitleshort()

            readfile = open('notes/40.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '5':
            clearscreen()
            metatitleshort()

            readfile = open('notes/50.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '6':
            clearscreen()
            metatitleshort()

            readfile = open('notes/60.py')
            print(readfile.read())
            readfile.close()
            break



        elif x == '7':
            clearscreen()
            metatitleshort()

            readfile = open('notes/70.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '8':
            clearscreen()
            metatitleshort()

            readfile = open('notes/90.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == '9':
            clearscreen()
            metatitleshort()

            readfile = open('notes/90.py')
            print(readfile.read())
            readfile.close()
            break


        elif x == '10':
            clearscreen()
            metatitleshort()

            readfile = open('notes/100.py')
            print(readfile.read())
            readfile.close()
            break

        elif x == 'e':
            clearscreen()
            metatitleshort()

            os.system('nano -T 4 notes/list_categories_.txt')
            print('0: Back to previous menu')

            break



        elif x == '0':
            exit()

        else:
            print('Must enter a number from 1 to 6 or 0 to exit')
            try:
                input("Press Enter to continue  0")  # Cheat to pause program
            except SyntaxError:
                pass





    y = 'z'
    while y != '0':


        print("\033[1;32;40m  ")  # Sets Text color to bright green
        y = input('                 Enter a number:  ')  # Accepts User Input
        print("\033[1;37;40m \n")  # Return to default text



        if y != '0':

            editor = 'nano -T 4'



            #os.system('nano -T 4 notes/'+y+'.py')

            #os.system(editor + ' notes/' + y + '.py')

            os.system('notepad' + ' notes/' + y + '.py' if os.name == 'nt' else editor + ' notes/'+y+'.py')

            if x == '1':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_Basic.txt')
                print(readfile.read())
                readfile.close()


            elif x == '2':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_GUI.txt')
                print(readfile.read())
                readfile.close()


            elif x == '3':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_Scraping.txt')
                print(readfile.read())
                readfile.close()


            elif x == '4':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_Django_Flask.txt')
                print(readfile.read())
                readfile.close()

            elif x == '5':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_CookBook.txt')
                print(readfile.read())
                readfile.close()


            elif x == '6':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_Hacking.txt')
                print(readfile.read())
                readfile.close()

            elif x == '10':
                clearscreen()
                metatitleshort()

                readfile = open('notes/list_categories_Recipes.txt')
                print(readfile.read())
                readfile.close()









        elif x == '0':
            pass

    '''                 No longer need, optional with pause created by using Nano
        try:
            input("Press enter to return to Menu")  # Cheat to pause the loop
        except SyntaxError:
            pass
    '''