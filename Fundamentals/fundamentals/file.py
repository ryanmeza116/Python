num1 = 42 #variable declaration, Numbers
num2 = 2.3 #variable declaration, 
boolean = True #variable declaration, Boolean
string = 'Hello World' #variable declaration, Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'], #variable declaration, Strings, initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, Boolean, Strings, initialize
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, Strings, initialize
print(type(fruit)) #log statement, access value
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms'), #Strings, add value
print(person['name']) #log statement, Strings
person['name'] = 'George' #, Strings
person['eye_color'] = 'blue' #, Strings
print(fruit[2]) #log statement

if num1 > 45: #type check, Numbers, if_conditional
    print("It's greater") #log statement, Strings
else:
    print("It's lower") #log statement, Strings, else

if len(string) < 5: #type check, length check, Numbers, if_conditional
    print("It's a short word!") #log statement, Strings
elif len(string) > 15: #type check, length check, Numbers, else if
    print("It's a long word!") #log statement, Strings
else:
    print("Just right!") #log statement, Strings, else

for x in range(5):#start-loop
    print(x) #log statement, Numbers, stop-loop
for x in range(2,5):#start-loop
    print(x) #log statement, Numbers, stop-loop
for x in range(2,10,3):#start-loop
    print(x) #log statement, Numbers, stop-loop
x = 0
while(x < 5):#type check, Numbers, start-while
    print(x) #log statement, Numbers, stop-loop, stop-while
    x += 1 #increment

pizza_toppings.pop() #delete value
pizza_toppings.pop(1)# delete value

print(person) #log statement,, access value
person.pop('eye_color')#, Strings
print(person) #log statement,, access value

for topping in pizza_toppings:#start-loop
    if topping == 'Pepperoni': #type check, Strings, access value
        continue # continue
    print('After 1st if statement') #log statement, Strings
    if topping == 'Olives':#type check, Strings, access value
        break #, stop-loop, break

def print_hello_ten_times():
    for num in range(10):#start-loop
        print('Hello') #log statement, Strings #log statement, stop-loop

print_hello_ten_times()

def print_hello_x_times(x): #function/ parameter = x
    for num in range(x):#start-loop
        print('Hello')#, Strings #log statement, stop-loop

print_hello_x_times(4) #function-called, argument = 4

def print_hello_x_or_ten_times(x = 10):#function, parameter = (x=10)
    for num in range(x):
        print('Hello')#, Strings #log statement, stop-loop

print_hello_x_or_ten_times() #function-called
print_hello_x_or_ten_times(4)#function-called// argument = 4


"""
Bonus section, multiline
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
#comment,  single line