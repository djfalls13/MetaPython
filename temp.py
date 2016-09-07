#!/usr/bin/env python3



teststuff = open('tmpstuff.txt', 'w')



teststuff.write('I want to be a programmer')



teststuff.close()



teststuff = open('tmpstuff.txt', 'a')

teststuff.write('\nand make good money')

teststuff.close()


x = open('tmpstuff.txt','r')

x = x.read()

print(x)
