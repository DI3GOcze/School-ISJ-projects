#!/usr/bin/env python3
import collections
from itertools import count
from traceback import print_tb

def log_and_count(**kwargs):
    def decorator(func):   
        counta = 0
        
        def inner(*args, **kwargs1):
            counta += 1
            print(counta)

            if 'key' in kwargs:
                kwargs["counts"][kwargs['key']] += 1
            else:
                kwargs["counts"][func.__name__] += 1
            
            print('called', func.__name__, 'with', args, 'and', kwargs1)
        return inner
    return decorator

my_counter = collections.Counter()

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b
 
f1(2, b=4)
