def evenIndexChar():
    
    s = input("Enter a string: ")
    for i in range(len(s)):
        if i % 2 == 0:
            print(s[i], end='')
    print()

evenIndexChar()
