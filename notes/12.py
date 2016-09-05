
import os



def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


clearscreen()

print('\n')

print('regular stuff')


print("\033[1;32;42m Bright Green ")


print('\n')

print("\033[0;37;40m back to default ")

print('regular stuff')


print("\033[1;32;42m Bright Green ")


'''
TEXT COLOR	CODE	    TEXT STYLE	CODE	BACKGROUND COLOR	CODE
Black	30	No effect	0	                Black	40
Red	    31	   Bold	    1	                Red	41
Green	32	Underline	2	                Green	42
Yellow	33	Negative1	3	                Yellow	43
Blue	34	Negative2	5	                Blue	44
Purple	35			                        Purple	45
Cyan	36			                        Cyan	46
White	37			                        White	47
'''