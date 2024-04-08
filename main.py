"""
OrderOfNumbers
"""
# Provide your solution here


n1 = input("Enter your first number:")
n2 = input("Enter your second number:")
sum = int(n1) + int(n2)

print(sum)
if int(n1) <= 0 or int(n2) <= 0:
    print("smaller or equal to 0")
elif int(n1) <= 0 and int(n2) <= 0:
    print("smaller or equal to 0")
elif int(n1) >= 0 and int(n2) >= 0 and int(n1) >= int(n2):
    print("error")

"""
SumUp
"""
# Provide your solution here
for i in range(3):    # For each number i in range 0-4. range(5) function returns list [0, 1, 2, 3, 4]
    num = input("Enter your number:")
    numbers = []
    numbers.append(num)