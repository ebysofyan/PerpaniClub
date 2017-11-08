import random

chars = '0123456789ABCDEF';

def generate_color(total):
    return ['#{0}'.format(''.join(random.choice(chars) for _ in range(6))) for value in range(0, total)]