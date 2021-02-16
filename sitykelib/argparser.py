import argparse

def start_argparse():
    parser = argparse.ArgumentParser(prog='SITYKE', description='Send It To Your Kindle Efficiently')

    parser.add_argument('-d', '--delete_output_files', action='store_true',
    help = 'Delete all the output files after the program ends')
    parser.add_argument('-i', '--ignore_translated_files', action='store_true',
    help = 'Ignore all translated files')
    parser.add_argument('-m', '--modify_pdf', action='store_true',
    help = 'Enable modification of output pdf with k2pdfopt')
    parser.add_argument('-c', '--cut_ppt', action='store_true',
    help = 'Cut the ppt files to fit the screen')
    parser.add_argument('-r', '--reform_doc', action='store_true',
    help = 'Reform doc files to fit the screen')
    parser.add_argument('-dm', '--dark_mode', action='store_true',
    help = 'Enable dark mode for devices that do not support it forcely')

    args = parser.parse_args()

    return args