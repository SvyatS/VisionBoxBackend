from string import ascii_uppercase, digits
from random import choice


def upload_user_avatar(instance, filename):
    return f'static/users/{instance.id}/avatar/{filename}'


def id_generator(size=8, chars=ascii_uppercase + digits):
    return ''.join(choice(chars) for _ in range(size))
