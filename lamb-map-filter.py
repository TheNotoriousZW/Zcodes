
sqrt = lambda x: x**0.5                            # lambda is an anonymous function can be set to unlimited parameters
                                                   # set the parameters before the : and the return value after
print(f"The square root is: {sqrt(9)}")            # can be called using () parenthesis

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
doublelist= list(map(lambda x: x*2, a))             # map function accepts a function and a list as its parameters
                                                   # can use lambda as the function in the map method
evenlist = list(filter(lambda x: x%2==0, a))      # filter out the false and return the conditions that is true
print(evenlist)
print(doublelist)

names = ['Zaphon Wray', 'Gary White', 'Kimar Evans', 'Fire Wray',
         'Zoriah Wray', 'Jackie Evans', 'Lyando Wray']

string = 'python 3'
print(string.split())                              # split method splits a string into a list

#names.sort(key=lambda x: x.split()[-1])            # for each string in the list the key splits the string into a list
                                                   # with the split method and sorts it by the last item in the list [-1]
                                                   # the last name
print(names)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}, {self.age}'


Lord_wray = person('Zaphon', '22')
junior = person('Junior', '25')
lyando = person('Lyando', '24')
kimar = person('Kimar', '30')

people = [junior, Lord_wray, lyando, kimar]
people.sort(key=lambda x: x.age)
print(people)

print((lambda x: (x % 2 and 'odd' or 'even'))(9))

string_check = lambda string: string in "Zaphon is the baddest man on the planet"

print(string_check('Zaphon'))

# map function - map(function, iterable)
#               - returns a iterator that applies a fucntion to every item of the iterable

def stripper(lst, index=1):                               # create a function that splits strings within a list
    splitter_lst = []
    stripper_lst =[]
    for elem in lst:
        splitter_lst.append(elem.split())
    for items in splitter_lst:
        stripper_lst.append(items[index])

    return stripper_lst


lastnames = list(stripper(names))
firstnames = list(stripper(names, 0))


print(list(filter(lambda x: x.startswith('E') , lastnames)))        # using the filter function to filter last names
