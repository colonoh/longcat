import random
import string

from sluggen.models import Slug


def generate(url, length):
    '''
    Given a URL, generate a new unique short string (a slug) of a given length.
    '''
    charset = string.ascii_letters + string.digits
    potential = ''.join((random.choice(charset) for i in range(length)))

    # if the slug exists, generate a new one
    while Slug.objects.filter(slug=potential).exists():
        print('generating a new slug because of a collision!!!')
        potential = ''.join((random.choice(charset) for i in range(length)))
    print(potential)

    return potential