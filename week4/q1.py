def sumSub(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
result = sumSub(num1, num2)
print(f"Addition: {result[0]}, Subtraction: {result[1]}")
