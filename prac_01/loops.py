"""
repeat i from 1 to 20 with step equal to 2
    print i
print()

repeat i from 0 to 100 with step equal to 10
    print i
print()

repeat i from 20 to 1 with step equal to -1
    print i
print()

get number of star
print number of star of "*"

get number of star
a = 1
repeat i from 1 to number of star
    print a of "*"
    a = a + 1
print()
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

number_of_star = int(input("Please enter number of star: "))
print("*" * number_of_star)

number_of_star = int(input("Please enter number of star: "))
a = 1
for i in range(number_of_star):
    print("*" * a)
    a += 1
print()
