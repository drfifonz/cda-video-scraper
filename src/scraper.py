import json
import re
import time
from random import choice

import requests
from bs4 import BeautifulSoup

import config as cfg


class Scraper:
    def __init__(self) -> None:
        self.headers = self._load_headers()

        # print(self._get_random_header())
        self.temp_header = self._get_random_header()

    def _load_headers(self) -> list[dict]:
        with open(cfg.HEADERS_PATH, "r") as file:
            return json.load(file)[cfg.HEADERS_SECTION]

    def _get_random_header(self) -> dict:
        return choice(self.headers)


scr = Scraper()
temp_h = scr.temp_header
# print(temp_h)

page_num = 1
max_pages = 1
search_qoute = "reksio"
url = f"https://www.cda.pl/video/show/{search_qoute}/p{page_num}?s=best"

# page = requests.get(url, headers=temp_h)
# print(page.status_code)
# doc = BeautifulSoup(page.text, "html.parser")


videos_dict = {}
for page_num in range(max_pages):
    url = f"https://www.cda.pl/video/show/{search_qoute}/p{page_num+1}?s=best"
    page = requests.get(url, headers=temp_h)
    doc = BeautifulSoup(page.text, "html.parser")

    if page.status_code != 200:
        print(f"Iteration: {page_num+1} breaks scrapping with code: {page.status_code}")
        break

    videos = doc.find_all(class_="video-clip")
    raw_links = [video.find_all(class_="video-clip-link autoHide")[0]["href"] for video in videos]
    links = [cfg.PAGE_URL + link[1:] for link in raw_links]
    raw_times = [video.find_all("a")[0].text for video in videos]
    times = [time_text.strip().split()[-1] for time_text in raw_times]
    titles = [video.find_all("a")[1].text for video in videos]
    # print(titles)
    # print(times)
    # for link in links:
    #     print(link[0]["href"])
    # print(videos)
    time.sleep(1)
# print(links)

videos_dict["title"] = titles
videos_dict["time"] = times
videos_dict["links"] = links


print("loop finished")
