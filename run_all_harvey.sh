# Insert Initialize Bash Script Text

# Insert Environment Initialization

cd scripts/digitalglobe_image_downloader/
python digitalglobe_scraper.py https://www.digitalglobe.com/opendata/hurricane-harvey/post-event
python digitalglobe_image_downloader url_tif_list Harvey
