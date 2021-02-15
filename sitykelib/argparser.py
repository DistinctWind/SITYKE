import argparse

def start_argparse():
    parser = argparse.ArgumentParser(prog='SITYKE', description='Send It To Your Kindle Efficiently')

    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--hello', action='store_true')

    args = parser.parse_args()

    return args