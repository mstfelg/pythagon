#!/usr/bin/env python3
'''CLAPS: Vector graphics convertor script'''
import argparse
import sys
import zipfile
from xml.etree.ElementTree import ElementTree
import GeoObj


parser = argparse.ArgumentParser(
    description="CLAPS: Vector graphics convertor script by Mustafa Alelg",
)
parser.add_argument("FILENAME",
                    action="store",
                    metavar="FILE",
                    nargs="+",
                    help="ggb file"
                    )
parser.add_argument("--output", "-o",
                    action="store",
                    dest="OUT_LANG",
                    default="asy",
                    help="Output file extension"
                    )
parser.add_argument("--decimal-points", "-d",
                    action="store",
                    dest="DECIPOINTS",
                    default=4,
                    help="Number of decimal places of free points"
                    )
opts = vars(parser.parse_args())


def main():
    """Entry point if called as an executable"""
    GeoObj(lang=opts['OUT_LANG']) # Set GeoObj language
    for file in opts['FILENAME']:
        if not '.' in file:
            file += '.ggb'
        elif file[-1] == '.':
            file += 'ggb'
        basename = file[:file.index('.')+1]
        sys.stdout = open(basename+opts['OUT_LANG'], 'w')

        try:
            ggb_tree = ElementTree().parse(
                zipfile.ZipFile(file).open("geogebra.xml")
            ).find("construction")
        except OSError:
            print(file, "is not found")
            sys.exit()

        print("/* --- Generated using Handysa --- */")
        print("/* ---", file[:-4], "--- */")

        last_obj = ""
        for obj in ggb_tree:
            # Defaults:
            out_args = [obj.get('label')]
            obj_type = obj.get('type')  # Points, numeric, function...
            cmd = obj.get('name')

            # CASE 1: command
            if obj.tag == "command":
                inp_args = [i[1] for i in obj.find('input').items()]
                out_args = [i[1] for i in obj.find('output').items()]
                obj_type = cmd  # cmd --> type in get_type

            # CASE 2: expression (e.g: M=A+B)
            elif obj.tag == "expression":
                inp_args = [obj.get('exp')]

            # CASE 3: free points (e.g: O=(0,0))
            # Check label to exclude dependent points
            elif obj_type == 'point' and out_args[0] != last_obj:
                coords = obj.find('coords')
                inp_args = ['(%.*f, %.*f)' % (
                    opts['DECIPOINTS'], float(coords.get('x')),
                    opts['DECIPOINTS'], float(coords.get('y'))
                )
                ]

            last_obj = out_args[-1]
            for i, arg in enumerate(out_args):
                if arg != "" and cmd is not None:  # Skip empty multi-outputs
                    print(conv.GeoObj(geotype=obj_type, out=arg, inp=inp_args, index=i))
                    print("%s%s=%s%s" % (conv.get_type(obj_type), arg,
                                         conv.get_cmd(cmd), conv.compose_args(inp_args)))

        sys.stdout.close()
print("\n")

if __name__ == "__main__":
    main()
