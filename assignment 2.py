'''You can use the following Python script to count the number of odd and even numbers in the given list:'''

#python
numbers = [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers count: ", even_count)
print("Odd numbers count: ", odd_count)


'''When you run this script, you'll get the following output:
Even numbers count:  6
Odd numbers count:  5
'''

