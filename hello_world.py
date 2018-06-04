"""
Simple program to say 'Hello world' and 'Good bye world' a number of times
"""

a = 1

for _ in range(10):
    if a < 5:
        print("Hello world")
    else:
        print("Good bye world")

    a += 1

