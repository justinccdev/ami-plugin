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
parser = MyParser('Summarize ami2-regex results')
parser.add_argument('-v', '--verbose', action="store_true", help="verbose output")
parser.add_argument('amiResultsPath', help='path to ami2-regex results.')
parser.add_argument('outFile', nargs='?', type=argparse.FileType('w'))
args = parser.parse_args()

count = 0
fileCount = 0
out = ""

for root, dirs, files in os.walk(args.amiResultsPath):
    for file in files:
        fileCount += 1
        path = "%s/%s" % (root, file)
        if 'regex' in path:
            if args.verbose:
                out = out + "### Processing %s ###\n" % path

            tree = ET.parse(path)
            results = tree.findall('result')
            resultsCount = len(results)
            count += resultsCount
        
            if resultsCount > 0:
                out = out + "Found %d results in %s\n" % (resultsCount, path)

                if args.verbose:
                    out = out + ET.tostring(tree.getroot()) + "\n"

out = out + "\nSUMMARY\n%d results from %d papers" % (count, fileCount)

if args.outFile:
  args.outFile.write(out)
else:
  print out
