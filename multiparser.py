'''
This is an example of parser with sub-parsers
'''

import argparse

def func_a(args: argparse.Namespace):
    assert set(vars(args).keys()).__contains__('va')
    if args.va:
        print("a: func_a called!")
    else:
        print("a: nothing to report")

def func_b(args: argparse.Namespace):
    assert set(vars(args).keys()).__contains__('vb')
    if args.vb:
        print("b: func_b called!")
    else:
        print("b: nothing to report")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Multi-parser")
    subparsers = parser.add_subparsers(help="sub-command help")

    # subparser a
    parser_a = subparsers.add_parser('a', description="Subparser a")
    parser_a.add_argument('-v', action="store_true", dest="va", help="print details")
    assert set(vars(parser.parse_args(['a'])).keys()) == {'va'}
    parser_a.set_defaults(func=func_a)
    assert set(vars(parser.parse_args(['a'])).keys()) == {'va', 'func'}

    # subparser b
    parser_b = subparsers.add_parser('b', description="Subparser b")
    parser_b.add_argument('-v', action="store_true", dest="vb", help="print details")
    assert set(vars(parser.parse_args(['b'])).keys()) == {'vb'}
    parser_b.set_defaults(func=func_b)
    assert set(vars(parser.parse_args(['b'])).keys()) == {'vb', 'func'}

    args = parser.parse_args()
    args.func(args)
