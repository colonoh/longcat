import random
import string

from sluggen.models import Slug


def generate(url, length):
    '''
    Given a URL, generate a new unique short string (a slug) for it.
    '''
    charset = string.ascii_letters + string.digits
    # TODO: replace with max length based on model
    potential = ''.join((random.choice(charset) for i in range(length)))

    # if Slug.objects.filter(slug=potential).exists():
        
    return potential