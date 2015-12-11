#!/usr/bin/python

# Example: python ami-regex-contact.py ../genome2010

import argparse
import ftplib
import gzip
import os
import xml.etree.ElementTree as ET

class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)

############
### MAIN ###
############
parser = MyParser('test')
parser.add_argument('resultsPath', help='path to ami2-regex results.')
parser.add_argument('outFile', nargs='?', type=argparse.FileType('w'))
args = parser.parse_args()

out = ""

for root, dirs, files in os.walk(args.resultsPath):
    for file in files:
        path = "%s/%s" % (root, file)
        if 'regex' in path:
            out = out + "### From %s ###\n" % path
            tree = ET.parse(path)
            out = out + ET.tostring(tree.getroot()) + "\n"

if args.outFile:
  args.outFile.write(out)
else:
  print out