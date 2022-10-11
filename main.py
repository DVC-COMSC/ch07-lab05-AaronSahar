
# ******************************
# Make your Code
# ******************************
strval = input().split()
numbers = list(map(int, strval))
print (numbers)
find_number = int(input("enter a number to be found: "))
print(numbers.count(find_number))