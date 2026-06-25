import hashlib

password = input("Enter your password: ")

def password_encryption(_password):
    return hashlib.shake_128(_password.encode()).hexdigest(10)

print(f"Data type: {type(password)}")
print(f"Encrypted password: {password_encryption(password)}")