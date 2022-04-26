import random
import string

print("Better Password Generator")

# skip a line :)

print("")

length=int(input("Enter the password length: "))

password = ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k = length))

print("")

print(f"Your password is: {password}")
