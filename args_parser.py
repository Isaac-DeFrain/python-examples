#!/usr/bin python3

import argparse

parser = argparse.ArgumentParser()

# parser.add_argument('-e', nargs='?', default=sys.stdout, help='encrypt')
# parser.add_argument('-d', nargs='?', default=sys.stdout, help='decrypt')
# parser.add_argument('-j', nargs='?', default=sys.stdout, help='json')

# creates nums positional var
parser.add_argument('nums', metavar='N', type=int, nargs='+', help='numbers to add')
parser.add_argument(
    '-s', dest='acc', action='store_const', const=sum, default=max, help='sum')

args = parser.parse_args()

# calls acc function declared on line 13 as dest
print(args.acc(args.nums))
