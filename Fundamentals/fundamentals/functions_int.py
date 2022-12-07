
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15

print("1: New X value : ", x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
students[0]['first_name'] = "Kobe-RIP"
print("2: Students Directory : ", students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0] = "Andres"
print("3: Sports Directory : ", sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]["y"] = 30
print("4 : New value of Z" , z)



'''
1. Change the value 10 in x to 15
2.Change the last_name of the first student from 'Jordan' to 'Bryant'
3.In the sports_directory, change 'Messi' to 'Andres'
4.Change the value 20 in z to 30
'''

'''
1. Created a function that given a list of dictionaries, function loops through each dict in list and prints key and value. 

'''

bible_books_and_authors = [
    {'book': 'Genesis', 'author': 'Moses'},
    {'book': 'Psalms', 'author': 'David and Various Others'},
    {'book': 'Romans', 'author': 'Apostle Paul'},
    {'book': 'Hebrews', 'author': 'Unknown'}
]
def iterateBible(list):
    for i in list:
        result = ""
        for k,v in i.items():
            result += f"{k} - {v}, "
        print("5: ", result)


iterateBible(bible_books_and_authors)

def iterate_keys(key_name, list):
    for i in list:
        for key in i.keys():
            if key == key_name:
                print(i[key_name])

    pass

iterate_keys('book',bible_books_and_authors)
iterate_keys('author',bible_books_and_authors)

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict):
    for i in dict.keys():
        print(f"{len(dict[i])} {i.upper()}")
        for x in dict[i]:
            print(x)

printInfo(dojo)


