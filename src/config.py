# SET BELOW PARAMETRS BEFORE FIRST RUN
DONWLOAD_PATH = "downloads"
FIREFOX_DRIVER_PATH = ""
FIREFOX_TO_DEV_NULL = "/dev/null"

PAGE_URL = "https://www.cda.pl/"
PAGE_SEARCH_URL = "https://www.cda.pl/video/show/"
PAGE_SEARCH_P = "p"
PAGE_SEARCH_SORT_TYPE = "?s=best"


HEADERS_PATH = "data/headers.json"
HEADERS_SECTION = "headers"

# dict keys
TITLES_DICT_KEY = "titles"
DURATION_DICT_KEY = "duration"
LINKS_DICT_KEY = "links"

# html elements' unique tags, used to find certain data

# static scraping with BeautifulSoup
HREF_TAG = "href"
A_TAG = "a"

VIDEO_CLASS_TAG = "video-clip"
LINK_CLASS_TAG = "video-clip-link autoHide"

# dynamic scraping with Selenium
TITLE_SEARCH_TAG = "h1"
LINK_SEARCH_TAG = "video"
LINK_ATTRIBUTE = "src"

# utils
REQ_SEARCH_URL = "cda.pl/info/"
REQ_SINGLE_VIDEO = "cda.pl/video/"
INPUT_MESSAGE = "Put videos numbers seperated by space only:"
INCORECT_INPUT_MESSAGE = "Incorect input."
