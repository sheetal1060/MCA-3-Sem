numbers = []

print("Enter 20 numbers:")
for i in range(20):
    num = int(input(f"Number {i + 1}: "))
    numbers.append(num)

print("Numbers divisible by 5:")
for num in numbers:
    if num % 5 == 0:
        print(num)
