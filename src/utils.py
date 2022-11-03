import config as cfg


class validator:
    def __init__(self) -> None:
        pass

    def is_search_url(url: str) -> bool:
        """
        Checking link is it search qoute url.
        """

        if url.find(cfg.REQ_SEARCH_URL) == -1:
            return False
        else:
            return True

    def is_single_video_url(url: str) -> bool:
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
    keys = list(videos.keys())

    for num in range(len(videos[keys[0]])):
        print(num + 1, end="\t")
        for key in range(len(keys)):
            if key == 0:
                print(f"{videos[keys[key]][num][:30]:30}", end="\t")
            else:
                print(f"{videos[keys[key]][num]:30}", end="\t")

        print("")


def get_user_videos_list(videos: dict) -> list:
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
