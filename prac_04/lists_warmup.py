"""
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0]
numbers[-1]
numbers[3]
numbers[:-1]
numbers[3:4]
5 in numbers
7 in numbers
"3" in numbers
numbers + [6, 5, 3]
3
2
1
[3, 1, 4, 1, 5, 9]
[1]
True
False
False
[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""
numbers = [3, 1, 4, 1, 5, 9, 2]
print(str(numbers[0]))

numbers[-1] = 1
print(numbers)

print(sum(numbers[2:]))

bools = []
for number in numbers:
    bools.append(number == 9)
print(bools)