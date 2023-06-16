"""
rhythms = input('Введите ритм: ').split()

def count_chars(word):
    chars = "aeiuyаеёиоуыэюя"
    count = 0
    for char in word:
        if char.lower() in chars:
            count += 1
    return count

def check(rhythms):
    counts = []
    for rhythm in rhythms:
        words = rhythm.split("-")
        count = sum(count_chars(word) for word in words)
        counts.append(count)
    return len(set(counts)) == 1

if(check(rhythms)):
    print('Парам пам-пам')
else:
    print('Пам-парам')

"""

def print_operatipn_table(operation, num_rows = 6, num_colums = 6):
    for row in range(1, num_rows + 1):
        for col in range(1, num_colums + 1):
            result = operation(row, col)
            print(f"{result}\t", end="")
        print()

def multiply(a, b):
    return a * b

print_operatipn_table(multiply, num_rows = 4, num_colums = 4)
