import argparse

def start_argparse():
    parser = argparse.ArgumentParser(prog='SITYKE', description='Send It To Your Kindle Efficiently')

    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--hello', action='store_true')

    parser.add_argument('-d', '--delete_output_files', action='store_true',
    help='Delete all the output files after the program ends')

    args = parser.parse_args()

    return args