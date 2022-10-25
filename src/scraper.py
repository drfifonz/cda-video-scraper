import json
import os
import re
import time
from random import choice

# from urllib import response

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

import requests
from bs4 import BeautifulSoup

import config as cfg


class Scraper:
    def __init__(self) -> None:
        self.driver_service = Service(executable_path=cfg.FIREFOX_DRIVER_PATH, log_path=cfg.FIREFOX_TO_DEV_NULL)

        self.headers = self._load_headers()

        self.temp_header = self._get_random_header()

    def _load_headers(self) -> list[dict]:
        with open(cfg.HEADERS_PATH, "r") as file:
            return json.load(file)[cfg.HEADERS_SECTION]

    def _get_random_header(self) -> dict:
        return choice(self.headers)

    def _get_data_from_one_page(self, url: str) -> dict:
        """
        Gets videos data specified by search quote from single page

        Returns dictionary of videos' :title, duration, link to video
        """
        videos_dict = {}

        page = requests.get(url, self._get_random_header())
        doc = BeautifulSoup(page.text, "html.parser")

        if page.status_code != 200:
            print(f" Breaks scrapping with code: {page.status_code}")
            return None

        videos = doc.find_all(class_=cfg.VIDEO_CLASS_TAG)

        raw_links = [video.find_all(class_=cfg.LINK_CLASS_TAG)[0][cfg.HREF_TAG] for video in videos]
        links = [cfg.PAGE_URL + link[1:] for link in raw_links]

        raw_duration = [video.find_all(cfg.A_TAG)[0].text for video in videos]
        duration = [time_text.strip().split()[-1] for time_text in raw_duration]

        titles = [video.find_all(cfg.A_TAG)[1].text for video in videos]

        videos_dict[cfg.TITLES_DICT_KEY] = titles
        videos_dict[cfg.DURATION_DICT_KEY] = duration
        videos_dict[cfg.LINKS_DICT_KEY] = links

        return videos_dict

    def get_data_from_pages(self, search_quote: str, pages_num: int = 1) -> dict:
        """
        gets videos data specified by search quote from certain pages number

        Returns dictionary of videos' :title, duration, link to video
        """
        # pages_num = 1

        videos_dict = {cfg.TITLES_DICT_KEY: [], cfg.DURATION_DICT_KEY: [], cfg.LINKS_DICT_KEY: []}
        for page_num in range(pages_num):

            url = os.path.join(
                cfg.PAGE_SEARCH_URL, search_quote, cfg.PAGE_SEARCH_P + str(page_num + 1) + cfg.PAGE_SEARCH_SORT_TYPE
            )

            one_page_videos_dict = self._get_data_from_one_page(url)

            videos_dict[cfg.TITLES_DICT_KEY] += one_page_videos_dict[cfg.TITLES_DICT_KEY]
            videos_dict[cfg.DURATION_DICT_KEY] += one_page_videos_dict[cfg.DURATION_DICT_KEY]
            videos_dict[cfg.LINKS_DICT_KEY] += one_page_videos_dict[cfg.LINKS_DICT_KEY]

            print(f"Data from page {page_num+1} collected.")
            time.sleep(1.5)
        return videos_dict

    def get_direct_video_url(self, url: str) -> list[str, str]:
        """
        Gets download link from video url.
        Return list of title & direct link to mp4 file.
        """

        with webdriver.Firefox(service=self.driver_service) as driver:
            driver.minimize_window()
            driver.get(url)

            title = driver.find_element(By.TAG_NAME, cfg.TITLE_SEARCH_TAG).text
            link = driver.find_element(By.TAG_NAME, cfg.LINK_SEARCH_TAG).get_attribute(cfg.LINK_ATTRIBUTE)
            return [title, link]

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
