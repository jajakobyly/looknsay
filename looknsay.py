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


if __name__ == "__main__":
    parser = ArgumentParser(description='Generate sequence of Look-and-Say numbers.')
    parser.add_argument('seed', type=int, nargs='?', default=1,
                        help='sequence seed')
    parser.add_argument('-i', '--iterations', dest='iterations', type=int, default=20,
                        help='number of iterations')

    args = parser.parse_args()

    print('Seed:', args.seed)
    print('Iterations:', args.iterations)

    for step in compute(args.seed, args.iterations):
        print(step)