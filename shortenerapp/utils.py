import string
import random


def url_generator(length=4, characters=string.ascii_letters + string.digits):
    return ''.join(random.choice(characters) for _ in range(length))


def short_url_creator(instance, length=4):
    created_url = url_generator(length=length)
    Myclass = instance.__class__
    qs_exists = Myclass.objects.filter(short_url=created_url).exists()
    if qs_exists:
        return short_url_creator(length=length)
    return created_url
