import random
import string

def generate_password(length=10):

    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

password = generate_password()
print(f"Generated Password: {password}")
