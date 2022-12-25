'''
This is an example of multiparser, a parser with sub-parsers
'''

import argparse

def func_a(args: argparse.Namespace):
    '''
    Asserts that when `parser_a` is invoked
    the namespace includes `va` flag and not `vb` flag
    '''
    assert set(vars(args).keys()).__contains__('va')
    assert not set(vars(args).keys()).__contains__('vb')
    if args.va:
        print("a: func_a called!")
    else:
        print("a: nothing to report")

def func_b(args: argparse.Namespace):
    '''
    Asserts that when `parser_b` is invoked
    the namespace includes `vb` flag and not `va` flag
    '''
    assert set(vars(args).keys()).__contains__('vb')
    assert not set(vars(args).keys()).__contains__('va')
    if args.vb:
        print("b: func_b called!")
    else:
        print("b: nothing to report")

if __name__ == '__main__':

    # multiparser
    parser = argparse.ArgumentParser(description="Multi-parser with subparsers a, b")
    subparsers = parser.add_subparsers(help="sub-command help")

    # subparsers
    # - subparser_a
    subparser_a = subparsers.add_parser('a', description="Subparser a")
    subparser_a.add_argument('-v', action="store_true", dest="va", help="print details")

    assert set(vars(parser.parse_args(['a'])).keys()) == {'va'}
    subparser_a.set_defaults(func=func_a)
    assert set(vars(parser.parse_args(['a'])).keys()) == {'va', 'func'}

    # - subparser_b
    subparser_b = subparsers.add_parser('b', description="Subparser b")
    subparser_b.add_argument('-v', action="store_true", dest="vb", help="print details")

    assert set(vars(parser.parse_args(['b'])).keys()) == {'vb'}
    subparser_b.set_defaults(func=func_b)
    assert set(vars(parser.parse_args(['b'])).keys()) == {'vb', 'func'}

    # dispatch appropriate subparser function
    args = parser.parse_args()
    args.func(args)
