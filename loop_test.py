fib_seq = (0, 1, 1, 2, 3, 5, 8, 13, 21)
name_list = ['Jessica', 'Paul', 'George', 'Henry', 'Adam']
name = 'Henry'

for x in fib_seq:
    print(x)

def sum(a, b, c):
    solution = a + b + c
    return print(solution)

sum(1, 2, 3)

y = lambda a, b, c : a + b + c
print(y(1, 2, 3))

for x in name_list:
    if x == 'Henry':
        print('Match found!')
    else:
        print('No Match') 


