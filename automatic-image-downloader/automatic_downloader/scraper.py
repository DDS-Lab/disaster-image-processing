import argparse
import os
import urllib2

from bs4 import BeautifulSoup

"""
Command line tool to scape the list of GeoTIFF file (.tif) download links
from DigitalGlobe Open Data Program: http://digitalglobe.com/opendata/

output: ../data/list.txt
"""

parser = argparse.ArgumentParser()
parser.add_argument('event_url', help="indicate the url of the event which \
you'd like to download images from")
args = parser.parse_args()

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(args.event_url)
# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')
# query out 'textarea' which is the html tag for the links
name_box = soup.findAll('textarea')

os.chdir('../data/')
text_file = open('list.txt', 'w+')
# write out to ../data/list.txt
for i in name_box:
    text_file.write(i.contents[0])
text_file.close
