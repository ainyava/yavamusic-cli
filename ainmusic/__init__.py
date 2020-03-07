from ainmusic.commands import Songs
from ainmusic.configs import config,ROOT_PATH

import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser(prog='ainmusic', description='Music tool by @ainyava.')

parser.add_argument('-f', '--file', nargs=1, help='Specify the songs list file.', metavar='file', dest='file')

parser.add_argument('-gl', '--get-list', nargs=1, help='Get list of an artist songs.', metavar='artist', dest='get_list')

parser.add_argument('-l', '--list', action='store_true', help='Prints the list of songs.')

parser.add_argument('-d', '--download', nargs=1, help='Download song from list.', metavar='id', dest='download_id')

parser.add_argument('-ft', '--fix-tags', nargs=1, help='Grap music metadata and cover and bind to file.', metavar='id', dest='fix_tags')

args = parser.parse_args()

def main():
    if len(sys.argv) == 1:
        parser.print_help()

    cwd = Path().absolute()

    songs = None
    if args.file:
        songs = Songs(config, cwd/args.file[0])

    if args.list:
        if args.file:
            songs.print_list()
        else:
            print('You must specify list file with -l, --list option.')
    elif args.get_list:
        songs.get_list(args.get_list[0])
    elif args.download_id:
        songs.download_item(int(args.download_id[0]))
    elif args.fix_tags:
        songs.fix_tags(int(args.fix_tags[0]))