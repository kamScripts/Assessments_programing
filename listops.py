
integer_list = [51, 50, 21, 5, 12, 7, 15, 9, 10, 70, 770, ]

def print_the_list(lis):
    print(*lis, sep=', ')

def sum_list(lis):
    result = 0
    for item in lis:
        result+=item
    print(f'sum of elements in the {lis} is {result}')

def print_largest(lis):
    print(max(lis))

def reverted_list(lis):
    print(lis[::-1])

def smallest_in_list(lis):
    result = lis[0]
    for item in lis:
        if item <= result:
            result = item
    print(result)
def smallest_functional(lis):
    print(min(lis))

print_the_list(integer_list)

sum_list(integer_list)

print_largest(integer_list)

reverted_list(integer_list)

smallest_in_list(integer_list)

smallest_functional(integer_list)
