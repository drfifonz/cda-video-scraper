import argparse
import time

import config as cfg
from scraper import Scraper
from utils import Validator, print_videos_dict, get_user_videos_selection_list, get_videos_by_list


def argument_parser():
    """
    Argument parser, returns parsed arguments.
    """
    arg_parser = argparse.ArgumentParser(description="cda.pl videos downloader")

    arg_parser.add_argument(
        "qoute", type=str, default=None, nargs="?", help="single video link / search video link / qoute to search video"
    )
    arg_parser.add_argument(
        "-p", "--pages", type=int, default=1, nargs="?", help="[OPTIONAL] number of scraping pages for search qoute"
    )

    return arg_parser.parse_args()


if __name__ == "__main__":
    parser = argument_parser()
    args = parser

    web_scraper = Scraper()
    validator = Validator()

    if validator.is_single_video_url(args.qoute):
        title, url = web_scraper.get_direct_video_url(args.qoute)
        print(f"DOWNLOADING VIDEO: {title} from {args.qoute} ")

        web_scraper.download_video(video_url=url, video_name=title.lower(), path=cfg.DONWLOAD_PATH)

        print("\nDONE")
        exit()
    elif validator.is_search_url(args.qoute):
        search_quote = str(args.qoute).split("/")[-1]
    else:
        search_quote = args.qoute

    videos = web_scraper.get_data_from_pages(search_quote=search_quote, pages_num=args.pages)

    print_videos_dict(videos)

    user_selection = get_user_videos_selection_list(videos)
    videos_url_list = get_videos_by_list(videos, user_selection)

    print("START DOWNLOADING: ")

    for url in videos_url_list:

        title, direct_url = web_scraper.get_direct_video_url(url)

        print(f"DOWNLOADING: {title.lower()}.mp4 from {url} ", end="")

        web_scraper.download_video(video_url=direct_url, video_name=title.lower(), path=cfg.DONWLOAD_PATH)
        time.sleep(2)

        print("DONE")
