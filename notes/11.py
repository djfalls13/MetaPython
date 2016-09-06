#ARGS --------------
'''
# This first version will not work
class argsGeneric():
    def normal_args(self, stuff ):
        for i in stuff:
            print(i)
x = argsGeneric()
x.normal_args('one', 'two','three')
'''

#This version works using the special *args to accept multiple arguments

grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
original_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas'] #untouched copy of grocery_list

dinner = ['Eggs','Mushrooms','Steak','Onion','Peppers']

lunch = ['Mayo','Ham','Bread','Lettuce']

class Munchies():

    def normal_args(self, *args ):


        for i in args:
            grocery_list.append(i)
            print(i)

    def foodfunction(self, morefood):
        for j in range(len(morefood)):  # Iterates through morefood List and appends it to grocery_list
            x.normal_args(morefood[j])

x = Munchies()

x.foodfunction(dinner)

print('This is the original list' , original_list)
print('This is the list appended with Dinner' , grocery_list)
x.foodfunction(lunch)
print('This is the list appended with Lunch' , grocery_list)


# KWARGS --------------

band = {}

tempdict = {}

class kwargsGeneric():
    def kwargs_example(self, **kwargs):
        for key, value in kwargs.items():
            print(key, value)
            band[key] = value

x = kwargsGeneric()

i = 0
while i < 3:

    a = input('Band Name: ')

    b = input('Genre: ')

    tempdict[a] = b

    print(tempdict)

    x.kwargs_example( **tempdict )

    i += 1

print(band)


x.kwargs_example(**band)