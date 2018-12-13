import argparse
from hexdump import hexdump
import strings_util


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar="F_NAME", type=str)
    parser.add_argument("-defs", help="Default drop out strings")
    parser.add_argument("--hex", help="Hex dump file with N(8 standard) shift in OUTPUT tool --hex N")
    parser.add_argument("--str", help="Drop out strings from file or use --str 'STRING' which use grep by 'STRING' chars")
    args = vars(parser.parse_args())
    if args['filename'] is not None:
        if args['hex'] is not None:
            hexdump(args['filename'], int(args['hex']))
        elif args['str'] is not None:
            strings_util.get_strings_from_file_grep(args['filename'], (args['str']))
        elif args['defs'] is not  None:
            strings_util.get_strings_from_file(args['filename'])
        else:
            hexdump(args['filename'], 8)


if __name__ == "__main__":
    Main()

