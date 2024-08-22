number = int(input("Enter an integer: "))

num_str = str(abs(number))

rev_digits = []

for digit in num_str[::-1]:
    rev_digits.append(int(digit))

print("Digits in reverse order:", rev_digits)
