from cryptography.fernet import Fernet
print("test")

key = Fernet.generate_key()


print(key)
