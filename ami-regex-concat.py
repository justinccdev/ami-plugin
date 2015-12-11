#!/usr/bin/python

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
args = parser.parse_args()

for root, dirs, files in os.walk(args.resultsPath):
    for file in files:
        path = "%s/%s" % (root, file)
        if 'regex' in path:
            print "### From %s ###" % path
            tree = ET.parse(path)
            print ET.tostring(tree.getroot())
