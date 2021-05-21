import requests
from bs4 import BeautifulSoup



def get_table():
    """
Scrape the table from liquipedia, and return list of dictionaries that represents the whole table
"""
    page = requests.get(
        "https://liquipedia.net/rocketleague/List_of_player_camera_settings")
    soup = BeautifulSoup(page.text, 'html.parser')

    cam_settings_table = soup.find(
        "table", {"class": "rl-responsive-table-sortable"}).find_all('tr')

    # First row is the header, just skip that.
    list_of_cam_settings = []
    for row in cam_settings_table[1:]:
        line = row.find_all('td')
        player_settings = {}
        for data in line:
            data_label = data['data-label']
            if data_label == "Player":
                name = data.find('b').find('a').get_text().strip()
                player_settings[data_label] = name
            elif data_label == "Team":
                span = data.find('span', {'class': 'team-template-text'})
                if span is None:
                    player_settings[data_label] = ''
                else:
                    player_settings[data_label] = span.find('a').get_text()
            else:
                player_settings[data_label] = data.get_text().strip()
        list_of_cam_settings.append(player_settings)
    return list_of_cam_settings
