from random import choice
import string

from sluggen.models import Slug

def get_random_string(length):
    charset = string.ascii_letters + string.digits
    return ''.join((choice(charset) for i in range(length))) 

def generate_new_slug(url, length):
    '''
    Given a URL, generate a new unique short string (a slug) of a given length.
    '''
    potential_slug = get_random_string(length)
    # if the slug exists, generate a new one
    while Slug.objects.filter(slug=potential_slug).exists():
        print('generating a new slug because of a collision!!!')
        potential_slug = get_random_string(length)

    return potential_slug