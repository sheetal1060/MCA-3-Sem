import secrets
import string

def generate_password(length=10):
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_symbols = string.punctuation
    all_characters = upper_case + lower_case + digits + special_symbols

  
    password = [
        secrets.choice(upper_case),         
        secrets.choice(upper_case),          
        secrets.choice(digits),              
        secrets.choice(special_symbols)      
    ]
    
    remaining_length = length - len(password)
    password += [secrets.choice(all_characters) for _ in range(remaining_length)]
    
    # Shuffle the password to ensure randomness
    secrets.SystemRandom().shuffle(password)
    
    # Convert list to string
    return ''.join(password)


print(f"Generated Password: {generate_password()}")
