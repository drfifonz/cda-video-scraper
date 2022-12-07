import os
import time

import config as cfg


class Validator:
    """
    Validates correctness of given url
    """

    def __init__(self) -> None:
        pass

    def is_search_url(self, url: str) -> bool:
        """
        Checking link is it search qoute url.
        """

        if url.find(cfg.REQ_SEARCH_URL) == -1:
            return False
        else:
            return True

    def is_single_video_url(self, url: str) -> bool:
        """
        Checking link is it video url.
        """

        if url.find(cfg.REQ_SINGLE_VIDEO) == -1:
            return False
        else:
            return True


def print_videos_dict(videos: dict) -> None:
    """
    Printing formatted videos dictionary.
    """
    keys_names = list(videos.keys())

    for num in range(len(videos[keys_names[0]])):
        print(num + 1, end="\t")
        for key in range(len(keys_names)):
            if key == 0:
                print(f"{videos[keys_names[key]][num][:30]:30}", end="\t")
            else:
                print(f"{videos[keys_names[key]][num]:30}", end="\t")

        print("")


def get_user_videos_selection_list(videos: dict) -> list:
    """
    geting list from user input of selected videos to download
    """

    print(cfg.INPUT_MESSAGE)

    while True:
        user_values = input()
        try:
            selected_list = [int(num) for num in user_values.split()]

            if max(selected_list) > len(videos.get(list(videos.keys())[0])):
                print(cfg.INCORECT_INPUT_MESSAGE)
                continue

            return selected_list
        except:
            print(cfg.INCORECT_INPUT_MESSAGE)
            continue


def get_videos_by_list(videos: dict, user_list: list) -> list[str]:
    """
    gets videos selected by list numbers and return list of videos url
    """
    keys_names = list(videos.keys())

    videos_list = []

    for user_id in user_list:
        # print("id: ", id)
        # print(videos[keys_names[2]][id - 1])
        # # return videos[keys_names[2]][id - 1]
        videos_list.append(videos[keys_names[2]][user_id - 1])
    return videos_list


def download_path() -> str:
    """
    returns string for download path in %Y-%m-%d-%H-%M-%S format
    """
    time_now = time.localtime()
    current_time = time.strftime("%Y-%m-%d-%H-%M-%S", time_now)

    return os.path.join(cfg.DONWLOAD_PATH, current_time)
