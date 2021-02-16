import argparse

def start_argparse():
    parser = argparse.ArgumentParser(prog='SITYKE', description='Send It To Your Kindle Efficiently')

    parser.add_argument('-d', '--delete_output_files', action='store_true',
    help = 'Delete all the output files after the program ends')
    parser.add_argument('-i', '--ignore_translated_files', action='store_true',
    help = 'Ignore all translated files')

    args = parser.parse_args()

    return args