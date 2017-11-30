from collections import namedtuple
from xml.etree import ElementTree

import requests

from service import min_episodes, get_episode, max_episode

Episode = namedtuple('Episode', 'title link pubdate show_id')
episode_data = {}


def main():
    show_header()

    download_data()

    # GET LATEST SHOW ID
    latest_show_id = max_episode()
    oldest_show_id = min_episodes()

    print("Working with total of {} episodes".format(latest_show_id))

    display_results()


def display_results():
    # DISPLAY RESULTS
    start = min_episodes()
    end = max_episode() + 1
    for show_id in range(start, end):
        # GET EPISODE
        info = get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def download_data():
    # DOWNLOAD THE EPISODE DATA
    url = 'https://talkpython.fm/episodes/rss'
    resp = requests.get(url)
    resp.raise_for_status()
    dom = ElementTree.fromstring(resp.text)
    episode_count = len(dom.findall('channel/item'))
    for idx, item in enumerate(dom.findall('channel/item')):
        episode = Episode(
            item.find('title').text,
            item.find('link').text,
            item.find('pubDate').text,
            episode_count - idx - 1
        )
        episode_data[episode.show_id] = episode


def show_header():
    # SHOW THE HEADER
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
