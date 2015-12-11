#!/usr/bin/python

import argparse
import ftplib
import gzip
import os
import os.path
import sys 

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
        if file == 'results.xml':
            print file
