#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 3 Assignment by Diandra Vega - Working with Regex"""


import csv
import re
import argparse
import os
import urllib2


PARSER = argparse.ArgumentParser()
PARSER.add_argument("--url", help="Add a URL to use in script.")
ARGS = PARSER.parse_args()


if ARGS.url:
    pass
else:
    print "No URL specified. Please see 'python assignment3.py' -h" +\
        " for help."
    os.system('python assignment3.py -h')
    exit()


def downloadData(filename=ARGS.url):
    """My docstring here"""
    response = urllib2.urlopen(filename)
    return response


def processData(readfile=downloadData()):
    "My docstring here"""
    data = csv.reader(readfile)
    filepaths = []
    browsers = []
    image_total = 0


    for row in data:
        filepaths.append(row[0])
        browsers.append(row[2])


    for fpath in filepaths:
        if re.search(r"\b\.([Jj][Pp][Ee]*[Gg]|[Pp][Nn][Gg]|[Gg][Ii][Ff])",
                fpath):
            image_total += 1
        else:
            pass


    return image_total


print processData()
