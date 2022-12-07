# looping through a string: 

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

# through a list: 

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

# looping in dicts : 
capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# WHILE loops : 
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

# ELSE 
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")



