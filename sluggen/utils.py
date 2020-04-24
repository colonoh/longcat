from random import choice
import string

from sluggen.models import Slug

def get_random_string(length):
    charset = string.ascii_letters + string.digits
    return ''.join((choice(charset) for i in range(length))) 

def generate_new_slug(length):
    '''
    Generate a new unique short string (a slug) of a given length.
    '''
    potential_slug = get_random_string(length)
    # if the slug aleady exists, generate a new one
    # note this will take longer and longer as more slugs are used, eventually
    # taking forever when all of them are used
    while Slug.objects.filter(pk=potential_slug).exists():
        print('generating a new slug because of a collision!!!')
        potential_slug = get_random_string(length)

    return potential_slug