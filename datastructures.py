"""
Cookbook for Data structures
"""

"""
Unpacking

Any sequence (or iterable) can be unpacked into variables using a simple assignment
operation. The only requirement is that the number of variables and structure match
the sequence.
"""

import datetime as dt


hd_deadline = str(dt.datetime(year=2018, month=6, day=30))

books_read = [
    ['Head first SD', 477, hd_deadline],
    ['Python cookbook', 700, hd_deadline]
]

random_list = ['pizza', 'dogs', 43, [12, 14, 25], ('list of crap', 23)]

for book in books_read:
    name, pages, deadline = book
    print("So far I am reading {}, it has {} pages and I need to finish it by {}.".format(name, pages, deadline))
    # Returns:
    # So far I am reading Head first SD, it has 477 pages and I need to finish it by 2018-06-30 00:00:00.
    # So far I am reading Python cookbook, it has 700 pages and I need to finish it by 2018-06-30 00:00:00.

# Number of variables need to match the number of items in iterable
food, pets, age, _, list1 = random_list

"""
Unpacking Elements from Iterables of Arbitrary Length
"""

# You don't know the n
food, pets, *random, list1 = random_list

print('Food I like: {}, pets I have: {}, random shit: {}, bullshit tuple: {}'.format(food, pets, random, list1))
# Returns: Food I like: pizza, pets I have: dogs, random shit: [43, [12, 14, 25]], bullshit tuple: ('list of crap', 23)


"""
Star unpacking can also be useful when combined with certain kinds of string processing
operations, such as splitting.
"""

line = 'nobody:*:-2:-2:Unpriviliged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print("Name: {}, random fields: {}, home directory: {}, sh: {}".format(uname, fields, homedir, sh))
# Returns:
# Name: nobody, random fields: ['*', '-2', '-2', 'Unpriviliged User'], home directory: /var/empty, sh: /usr/bin/false


"""
Unpacking list with head and tail
"""

items = [1, 10, 7, 4, 5, 9]
head, *tail = items


def sum(items):
    # Recursive algorithm
    head, *tail = items
    return head + sum(tail) if tail else head

print(sum(items))
# Prints 36


"""
Keeping the last N items
module: collections
method: deque

Keeping a history
"""

from collections import deque


"""
Creating iteration patterns with Generators
Using yield
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


list_floats = list(frange(0, 10, 0.5))
print(list_floats)

