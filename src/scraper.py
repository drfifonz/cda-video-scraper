import json
import os
import re
import time
from random import choice
from urllib import response

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup

import config as cfg


class Scraper:
    def __init__(self) -> None:
        self.headers = self._load_headers()

        self.service = Service(executable_path="resources/geckodriver-v0.31.0-linux64/geckodriver")

        self.temp_header = self._get_random_header()

    def _load_headers(self) -> list[dict]:
        with open(cfg.HEADERS_PATH, "r") as file:
            return json.load(file)[cfg.HEADERS_SECTION]

    def _get_random_header(self) -> dict:
        return choice(self.headers)

    def get_data_from_one_page(self, url: str) -> dict:
        videos_dict = {}

        page = requests.get(url, self._get_random_header())
        doc = BeautifulSoup(page.text, "html.parser")

        if page.status_code != 200:
            print(f" breaks scrapping with code: {page.status_code}")
            return None

        videos = doc.find_all(class_="video-clip")
        raw_links = [video.find_all(class_="video-clip-link autoHide")[0]["href"] for video in videos]
        links = [cfg.PAGE_URL + link[1:] for link in raw_links]
        raw_times = [video.find_all("a")[0].text for video in videos]
        times = [time_text.strip().split()[-1] for time_text in raw_times]
        titles = [video.find_all("a")[1].text for video in videos]

        videos_dict["titles"] = titles
        videos_dict["times"] = times
        videos_dict["links"] = links

        # time.sleep(1)
        return videos_dict

    def get_data_from_pages(self, search_phrase: str, pages_num: int = 1) -> dict:
        # pages_num = 1
        videos_dict = {"titles": [], "times": [], "links": []}
        for page_num in range(pages_num):
            url = f"https://www.cda.pl/video/show/{search_phrase}/p{page_num+1}?s=best"

            one_page_videos_dict = self.get_data_from_one_page(url)
            # print(page_num)
            # print(url, "\n")
            videos_dict["titles"] += one_page_videos_dict["titles"]
            videos_dict["times"] += one_page_videos_dict["times"]
            videos_dict["links"] += one_page_videos_dict["links"]
            # print(dictionary["titles"])
            print(f"Data from page {page_num+1} collected.")
            time.sleep(1.5)
        return videos_dict

    def download_video(self, video_url: str, video_name: str, path: str) -> None:
        if not os.path.exists(path):
            os.mkdir(path)

        file_path = os.path.join(path, f"{video_name}.mp4")
        print(file_path)
        try:
            response = requests.get(video_url, self._get_random_header())
            with open(file_path, "xb") as file:
                file.write(response.content)
        except:
            print(f"{video_name} already exists.")

    def get_direct_video_url(self, url: str) -> list[str, str]:
        with webdriver.Firefox(service=self.service) as driver:
            driver.minimize_window()
            driver.get(url)

            title = driver.find_element(By.TAG_NAME, "h1").text
            link = driver.find_element(By.TAG_NAME, "video").get_attribute("src")
            return [title, link]
