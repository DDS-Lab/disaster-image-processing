import argparse
import os
import urllib.request


"""
Command line tool to easily download a batch of GeoTIFF files (.tif)
from DigitalGlobe's Open Data Program: http://digitalglobe.com/opendata/
Input files: ../data/list.txt
Output files: ../data/<hurricane_name>
"""


def download_files(urls, overwrite_if_exists=False):
    for fileUrl in urls:
        filename = fileUrl[fileUrl.rfind("/")+1:]
        if overwrite_if_exists or not os.path.isfile(filename):
            urllib.request.urlretrieve(fileUrl, filename)
            print('downloaded file: {}'.format(filename))


def filter_list_by_extension(urls, extension):
    result = []
    for fileUrl in urls:
        if fileUrl.endswith(extension):
            result.append(fileUrl)
            print('added to queue: {}'.format(fileUrl))
    return result


# execution starts here. command line args processing.
parser = argparse.ArgumentParser(epilog='Each URL must be on a new line.')
parser.add_argument('urls', help='add the file name in the ../../data \
folder here with the list of urls')
parser.add_argument('hurricane_name', help='identify the hurricane name here to\
 label the output folder in ../../data')
args = parser.parse_args()

os.chdir('../../data/download_list/')
file_list = args.urls
with open(file_list) as f:
    event = args.hurricane_name
    if not os.path.isdir('../%s' % event):
        os.mkdir('../%s' % event)
    os.chdir('../%s' % event)
    content = f.readlines()
    # remove whitespace characters at the end of each line
    content = [x.strip() for x in content]
    tiffList = filter_list_by_extension(content, '.tif')
    download_files(tiffList)
