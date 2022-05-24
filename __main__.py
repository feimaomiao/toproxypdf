import argparse
from ast import arg
import glob
import logging
import os
from PIL import Image
from os import path

def parse_arguments() -> dict:
    """Parses user inputted arguments

    Raises:
        FileNotFoundError: required position argument "file" is not an existing directory

    Returns:
        dict: returns a dict consisting of the input folder, output file, excluded filenames and verbosity.
    """
    parser = argparse.ArgumentParser(prog="toproxypdf", epilog="If you think a bug has occured, please open an issue at https://github.com/feimaomiao/toproxypdf/issues")
    parser.add_argument("folder", help="folder path where all your images are stored")
    parser.add_argument("-o", "--output", help="output pdf file name", dest="output")
    parser.add_argument("-e", "--exclude", help="File names that should be excluded (in short os form)", action = "extend", dest="excluded", nargs="+")
    # verbose and quiet cannot coexist
    pgroup = parser.add_mutually_exclusive_group()
    pgroup.add_argument("-v", "--verbose", help="increaes output verbosity", action="store_true")
    pgroup.add_argument("-q", "--quiet", help="reduces output verbosity", action="store_true")
    args = parser.parse_args()
    a = {
        # input folder
        "folder"    : args.folder,
        # output file 
        "output"    : args.output if args.output is not None else f"{args.folder}.pdf",
        # list of excluded file names
        "excluded"  : args.excluded,
    }
    verbosity = {
        0: logging.CRITICAL,
        1: logging.INFO,
        2: logging.DEBUG
    }
    logging.basicConfig(level=verbosity[0 if args.quiet else 2 if args.verbose else 1])
    if not path.isdir(a["folder"]):
        raise FileNotFoundError(f"\'{a['folder']}\' is not a folder.")
    return a

def list_files(arguments: dict) -> list:
    # list all excluded files
    excluded_files = []
    for fn in arguments['excluded']:
        excluded_files += glob.glob(path.join(arguments['folder'], fn))
        
    for files in sorted(os.listdir(arguments['folder'])):
        fn = path.join(arguments['folder'], files)
        logging.debug(f"Verifying image {fn}")
        if not os.path.isfile(fn):
            logging.info(f"{fn} is not a file, will be skipped")
            continue
        img= Image.open(fn)
        try:
            img.verify()
        except:
            logging.info(f"{fn} is not a valid image, will be skipped")
        
        


if __name__ == "__main__":
    arguments = parse_arguments()
    files_to_load = list_files(arguments)