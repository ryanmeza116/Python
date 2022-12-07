print("Hello World")
print(type('Hello World!'))

name = "ryan"
jedi = "Obi-Wan Kenobi"
general = "General Grievous"
lightsaber = 1
print(f"Hello, {name}")

def general_kenobi():
    print("Hello There")
    print("General " + jedi)
    print(str(lightsaber) + " Lightsaber to add to my collection")

print(general_kenobi())

favorite_number = 69 #nice
print("Hello ", favorite_number) #This wont work
print("Hello" + str(favorite_number)) #this will work

favorite_food_one = "burritos"
favorite_food_two = "tacos"

print("I love to eat ", favorite_food_one , "and ", favorite_food_two)
print(f"I love to eat{favorite_food_two} and {favorite_food_one}")