for x in range (0,151):
    print(x)

for x in range(0,1005,5):
    print(x)

for x in range(0,101):
    if x % 10 == 0: 
        print('Coding Dojo')
    elif x % 5 == 0:
        print('Coding')
    else:
        print(x)

for x in range(2018,0,-4):
    print(x)

low_num = 2
high_num = 9
mult = 3

for i in range(low_num, high_num+1):
    if i%mult == 0:
        print(i)

# num = 0
# for x in range(0,500001):
#     while x % 2 != 0:
#         num = num + x
#         print(num)
#         print(x)
num = 0
for x in range(1,500001):
    if x%2 == 1:
        num = num + x
        print("num is", num)
        print(x)
print("total is", num)


