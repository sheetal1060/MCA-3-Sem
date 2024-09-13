import secrets

def generate_otp():
    otp = secrets.randbelow(900000) + 100000
    return otp


otp = generate_otp()
print(f"Your OTP is: {otp}")
