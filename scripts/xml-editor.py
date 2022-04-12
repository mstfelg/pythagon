import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(
	description = "GeoGebra script library by Mustafa Alelg",
)
parser.add_argument("FILENAME",
    action = "store",
    metavar = "FILE",
    nargs = "+",
    help = "xml file"
)
opts = vars(parser.parse_args())
root = ET.fromstring("""<?xml version="1.0" encoding="utf-8"?>
<geogebra format="5.0" version="5.0.627.0" app="classic" platform="d"  xsi:noNamespaceSchemaLocation="http://www.geogebra.org/apps/xsd/ggt.xsd" xmlns="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" >
</geogebra>
""")
for filename in opts['FILENAME']:
    with open(filename, 'r') as file:
        root.append(file.read())
