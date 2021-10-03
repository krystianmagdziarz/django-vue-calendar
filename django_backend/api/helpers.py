import random


def generate_color():
    while True:
        yield "#"+''.join([random.choice('0123456789ABCDEF') for x in range(6)])
