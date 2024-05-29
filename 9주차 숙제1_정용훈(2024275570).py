#f(xs) for xs in iter
#f(xs) for xs in iter if pred(xs)

#1부터 5까지 정수 리스트 만들기
number_list_1 = []
number_list_1.append(1)
number_list_1.append(2)
number_list_1.append(3)
number_list_1.append(4)
number_list_1.append(5)
print('number_list_1 = ',number_list_1)

number_list_2 = []
for number in range(1, 6):
    number_list_2.append(number)
print('number_list_2 = ',number_list_2)

number_list_3 = list(range(1,6))
print('number_list_3 = ',number_list_3)

#1부터 5까지의 정수 리스트 만들기 - List comprehension
number_list_4 = [number for number in range(1,6)]
print('number_list_4 = ', number_list_4)

number_list_5 = [number-1 for number in range(1,6)]
print('number_list_5 = ',number_list_5)

a_list_1 = [number for number in range(1, 6) if number % 2 == 1]
print('a_list_1 = ', a_list_1)

a_list_2 = []
for number in range (1, 6):
    if number%2 == 1:
        a_list_2.append(number)
print('a_list_2 = ', a_list_2)

sentence = ['I', 'Love','Python', 'Soooooo', 'MUCH!!!']
#함수 적용
functions = [word.lower() for word in sentence]
#조건 적용
joguns = [word for word in sentence if len(word) > 6]
#함수 적용하여 튜플로 저장
tuples = [(x, x**2, x**3) for x in range(10)]

rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

rows_2 = range(1,4)
cols_2 = range(1,3)
cells_2 = [(row,col) for row in rows_2 for col in cols_2]
for cell in cells_2:
    print(cell)

List_Comprehension = [(i,j) for i in range(5) for j in range(i)]
print(List_Comprehension)

#Dictionary comprehension
#{key_func(vars):val_func(vars) for vars in iterable}

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts_2 = {letter: word.count(letter) for letter in word}
print(letter_counts_2)

letter_counts_3 = {letter:word.count(letter) for letter in set(word)}
print(letter_counts_3)

#{func(vars) for vars in iterable
a_set = {number for number in range(1,6) if number % 3 ==1}
print(a_set)

def function_name(param1, param2):
    value = do_somthing()
    print(value)
    return value

def sum(a,b):
    return a+b

print(sum(1,2))
print(sum(1.3, 3.1))
print(sum('love ', 'python'))

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredt'

lists_zip = list(zip(english, french))
print(lists_zip)
dicts_zip = dict(zip(english, french))
print(dicts_zip)

#wine, entree, dessert를 받아서 딕셔너리로 만들어 반환하는 함수
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
#함수호출
menus_2 = menu('chardonnay', 'chicken', 'cake')
print(menus_2)

menus_3 = menu(entree='beef', dessert='bagel', wine='bordeaux')
print(menus_3)

menus_4 = menu('fronteanc', dessert='flan', entree='fish')
print(menus_4)

def menu2(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menus_5 = menu2('chardonnay', 'chicken')
print(menus_5)

menus_6 = menu2('dunkelfelder', 'duck', 'doughnut')
print(menus_6)

def menu3(price, wine='chardonnay', entree='chicken', dessert='pudding'):
    return{'price': price, 'wine': wine, 'entree': entree, 'dessert': dessert}

print(menu3(100))
print(menu3(price=100))
print(menu3(price=120, entree='beef'))
print(menu3(dessert='bagel', price=110))
print(menu3('eighty', 'saint-pierre', 'fish'))
print(menu3('hundred', wine='saint-pierre'))

def menu4(price, wine='chardonnay', entree='chicken', dessert='pudding'):
    return{'price':price, 'wine':wine, 'entree':entree, 'dessert':dessert}

#print(menu4())
#print(menu4(price=100, 'saint-pierre'))
#print(menu4(100, price=120))
#print(menu4(main='cream pasta'))

def echo(anything):
    'echo returns its input argument'
    return anything

def print_if_true(thing, check):
    """
    prints the first argument if a second argument is true.
    the operation is :
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
        """
    if check:
        print(thing())

help(echo)