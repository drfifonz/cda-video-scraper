from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import requests
import re
from bs4 import BeautifulSoup

import argparse


def argument_parser():
    parser = argparse.ArgumentParser(description="cda.pl videos downloader")

    return parser


if __name__ == "__main__":
    parser = argument_parser()
    opts = parser.parse_args
