import random
import string

def pas():
    collection = string.ascii_letters + string.digits + string.punctuation

    password = random.choice(string.digits)

    password += random.choice("@#$%&")

    for i in range(8):
        password += random.choice(collection)

    lst = list(password)

    random.SystemRandom().shuffle(lst)
    password = ''.join(lst)
    return password

print(pas())