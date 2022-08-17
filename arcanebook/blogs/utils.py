
import random
import string
from django.utils.text import slugify


def random_text_gen(n):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits,k=n))
    return res

def slug_generator(text):
    new_slug = slugify(text)
    # we need to check slug exists or not
    from .models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).exists():
        new_slug = new_slug + random_text_gen(8)
    else:
        pass
    return new_slug