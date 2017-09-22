# Techno Twitter Helper Functions

import requests
import xml.etree.ElementTree as ET


def get_playlist_html_content(url):
    html_content = requests.get(url)
    print("Got Html Content")
    if not html_content:
        print("There was no HTML content!")
        return False
    else:
        print("There was html content");
        return html_content


if __name__ == "__main__":
    get_playlist_html_content("https://soundcloud.com/ssedky14/sets/techno")
