#!/usr/bin/env python3
import json
import os
import plistlib
import tempfile
import uuid
import zipfile

import click


def read_plist(filename):
    with open(filename, 'rb') as plist_file:
        plist_entry = plistlib.load(plist_file)
    return plist_entry


def gen_uuid():
    return str(uuid.uuid4())


def plist_to_alfred(plist_entry):
    alfred_entry = []
    for entry in plist_entry:
        temp_dict = dict()
        temp_dict["snippet"] = entry["phrase"]
        temp_dict["uid"] = gen_uuid()
        temp_dict["name"] = entry["shortcut"][1:]
        temp_dict["keyword"] = entry["shortcut"]
        snippet = {"alfredsnippet": temp_dict}
        alfred_entry.append(snippet)
    return alfred_entry


def save_json(entry):
    filename = entry["alfredsnippet"]["name"] + " " + entry["alfredsnippet"]["uid"] + ".json"
    with open(filename, "w") as outfile:
        json.dump(entry, outfile)
    return outfile.name


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename):
    """Convert plist text substitution to Alfred Snippets (2017 by CarlosEvo)

    Small tool which reads maxOS text substitution plist files and generates an Alfred (3,x) snippet collection.

    The script will work in a temporary directory and move the resulting .alfredsnippets file back to the directory it is invoked from.

    """

    plist_entry = read_plist(filename)
    alfred_entry = plist_to_alfred(plist_entry)
    current_dir = os.getcwd()
    with tempfile.TemporaryDirectory() as temp_dir:
        os.chdir(temp_dir)
        file_list = []
        for entry in alfred_entry:
            file_list.append(save_json(entry))
        output_filename = filename[:-6] + '.alfredsnippets'
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
            for entry in file_list:
                zf.write(entry)
            zf.close()
        os.rename(output_filename, os.path.join(current_dir, output_filename))


if __name__ == '__main__':
    main()
