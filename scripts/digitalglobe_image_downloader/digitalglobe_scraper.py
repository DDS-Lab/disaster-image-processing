import argparse
import os
import requests

from bs4 import BeautifulSoup

"""
Command line tool to scape the list of GeoTIFF file (.tif) download links
from DigitalGlobe Open Data Program: http://digitalglobe.com/opendata/
This script only scrapes either pre-event or post-event for the hurricane you
select.
input: url of the hurricane tif links
output: ../data/url_tif_list.txt
usage:
'python digitalglobe_scraper.py\
 https://www.digitalglobe.com/opendata/hurricane-harvey/post-event'
"""


def no_return_error(links):
    if len(links) == 0:
        raise Exception('This DigitalGlobe website does not have any image\
 download links')


def get_img_links(page_url):
    # query the website and return the html to the variable 'page'
    page = requests.get(page_url)
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page.content, 'html.parser')
    # query out 'textarea' which is the html tag for the links
    links = soup.findAll('textarea')

    no_return_error(links)

    if not os.path.isdir('../../data'):
        os.mkdir('../../data')

    if not os.path.isdir('../../data/download_list/'):
        os.mkdir('../../data/download_list/')
    os.chdir('../../data/download_list/')
    # write out to ../data/url_tif_list.txt
    with open('url_tif_list.txt', 'w+') as text_file:
        for i in links:
            text_file.write(i.contents[0])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('event_url', help="indicate the url of the event which \
you'd like to download images from")
    args = parser.parse_args()
    page_url = args.event_url
    get_img_links(page_url)
