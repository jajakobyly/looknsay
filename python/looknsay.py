#!/usr/bin/env python3

from argparse import ArgumentParser
from itertools import groupby


def iterate(n):
    result = 0
    digits = [int(i) for i in str(n)]
    for k, g in groupby(digits):
        result = result * 100 + len(tuple(g)) * 10 + k
    return result


def compute(n, i=20):
    yield n
    x = n
    for i in range(0, i):
        x = iterate(x)
        yield x


def last_item(iter):
    item = None
    for item in iter:
        pass
    return item


if __name__ == "__main__":
    parser = ArgumentParser(description='Generate sequence of Look-and-Say numbers.')
    parser.add_argument('seed', type=int, nargs='?', default=1,
                        help='sequence seed')
    parser.add_argument('-i', '--iterations', dest='iterations', type=int, default=20,
                        help='number of iterations')
    parser.add_argument('-last', '--only-last', action='store_true',
                        help='print only last step of the iteration')

    args = parser.parse_args()
    computer = compute(args.seed, args.iterations)

    if not args.only_last:
        for step in computer:
            print(step)
    else:
        print(last_item(computer))