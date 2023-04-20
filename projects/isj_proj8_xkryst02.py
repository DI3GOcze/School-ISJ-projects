#!/usr/bin/env python3
import cProfile

# Priklad 6
def first_with_given_key_test(iterable, key=lambda x: x):
    processed = set()

    for item in iterable:
        if key(item) not in processed:
            processed.add(key(item))
            yield item


def first_with_given_key_dict(iterable, key=lambda func: func):
    used_keys_list = dict()

    for i in iterable:
        key_value = key(i)
        if not key_value in used_keys_list:
            used_keys_list[key_value] = 1
            yield i


def first_with_given_key(iterable, key=lambda func: func):
    used_keys_list = list()
    return_values = list()
    for i in iterable:
        key_value = key(i)
        if not key_value in used_keys_list:
            return_values.append(i)
            used_keys_list.append(key_value)

    return return_values


def test():
    ret = list()
    for i in range(10000):
        tmp = list()
        for j in range(i):
            tmp.append(j)
        ret.append(tmp)

    return ret

ret = test()

cProfile.run('list(first_with_given_key_dict(ret, key = len))')