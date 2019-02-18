#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 3 Assignment by Diandra Vega - Working with Regex"""


import csv
import re
import argparse
import os
import urllib2


PARSER = argparse.ArgumentParser()
PARSER.add_argument('--url', help='Add a URL to use in script.')
ARGS = PARSER.parse_args()


if ARGS.url:
    pass
else:
    print "No URL specified. Please see 'python assignment3.py' -h" +\
        " for help."
    os.system('python assignment3.py -h')
    exit()


def downloadData(fileurl):
    """This function downloads data from a URL.

    ARGS:
        fileurl (str): This will be the URL to download a file from.

    RETURNS:
        instance: Returns instance of urlopen class from urllib2 module
            with contents of downloaded file.

    EXAMPLES:
        >>> downloadData('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')
    """
    response = urllib2.urlopen(fileurl)
    return response


def processData(readfile=downloadData(ARGS.url)):
    """This will take the contents from downloaded URL which should include
    a CSV file. The CSV file's data is then processed to check for how
    many fields in first column are images and what is the most popular
    browser used.

    ARGS:
        readfile (instance): Parameter passed should be instance of downloaded
            URL from downloadData(). Defaults to downloadData(ARGS.url).

    RETURNS:
        string: Returns are two lines of strings reporting percentage of images
            in the requests from CSV file and what was the most widely used
            browser tallied.

    EXAMPLES:
        >>> processData(downloadData('
        http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'))
        Image requests account for 78.77% of all requests.
        Chrome is the most used web browser.
    """
    browsers = []
    browser_used = {'Chrome': 0, 'Firefox': 0, 'Internet Explorer': 0}
    data = csv.reader(readfile)
    filepaths = []
    image_total = 0


    for row in data:
        filepaths.append(row[0])
        browsers.append(row[2])


    for images in filepaths:
        if re.search(r'\b\.([Jj][Pp][Ee]*[Gg]|[Pp][Nn][Gg]|[Gg][Ii][Ff])',
                     images):
            image_total += 1
        else:
            pass


    for browser in browsers:
        regex_str = r'([Cc]hrome|[Ff]irefox|[Mm][Ss][Ii][Ee])'
        b_type = re.search(regex_str, browser)

        if b_type:
            if b_type.group() == 'Chrome':
                browser_used['Chrome'] += 1
            elif b_type.group() == 'Firefox':
                browser_used['Firefox'] += 1
            elif b_type.group() == 'MSIE':
                browser_used['Internet Explorer'] += 1
        else:
            pass


    image_percentage = (float(image_total) / float(10000)) * 100
    image_results = 'Image requests account for {percentage}% of all requests.'.format(
        percentage=image_percentage)
    b_most_used = max(browser_used, key=browser_used.get)
    b_results = '{browser} is the most used web browser.'.format(
        browser=b_most_used)


    return image_results + '\n' + b_results


print processData()
