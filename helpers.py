
import random
import string


def generate_user_data():
    email = f"test-email-{random.randint(1, 10000)}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    name = f"TestUser{random.randint(1, 100)}"
    return {
        "email": email,
        "password": password,
        "name": name
        }
