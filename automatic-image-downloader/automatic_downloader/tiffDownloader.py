import sys
import urllib
import os
import os.path


"""
Command line tool to easily download a batch of GeoTIFF files (.tif)
from DigitalGlobe Open Data Program: http://digitalglobe.com/opendata/
"""


def download_files(urls, overwrite_if_exists=False):
    for fileUrl in urls:
        filename = fileUrl[fileUrl.rfind("/")+1:]
        if overwrite_if_exists or not os.path.isfile(filename):
            opener = urllib.URLopener()
            opener.retrieve(fileUrl, filename)
            print('downloaded file: {}'.format(filename))


def filter_list_by_extension(urls, extension):
    result = []
    for fileUrl in urls:
        if fileUrl.endswith(extension):
            result.append(fileUrl)
            print('added to queue: {}'.format(fileUrl))
    return result


# execution starts here. command line args processing.
if len(sys.argv) == 2 and sys.argv[1] == '-h':
    print('\n\n   Usage: python tiffDownloader.py <urls_file> <hurricane_name> \n\n   Each URL must be on a new line.')
elif sys.argv[1] and sys.argv[2]:
    os.chdir('../data')
    file_list = sys.argv[1]
    with open(file_list) as f:
        event = sys.argv[2]
        print ('../data/%s' % event)
    #     os.mkdir('../data/@event')
    #     os.chdir('../data/@event')
    #     content = f.readlines()
    #     # remove whitespace characters at the end of each line
    #     content = [x.strip() for x in content]
    #     tiffList = filter_list_by_extension(content, '.tif')
    #     download_files(tiffList)
else:
    print('error: required command line argument missing. \n\n Syntax: python httpDownloader.py <urls_file> '
          '<hurricane_name> \n\n Each URL must be on a new line.')
    sys.exit(0)
