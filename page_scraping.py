import requests
from bs4 import BeautifulSoup
import customize_settings



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
            # Liquipedia accidently nested a nav table into the settings one.
            # Sorry to whoever's mistake I'm documenting probably forever.
            try:
                data_label = data['data-label']
            except:
                break
            if data_label == "Player":
                name = data.find('b').find('a').get_text().strip()
                player_settings[data_label] = name
            elif data_label == "Team":
                try:
                    span = data.find('span', {'class': 'team-template-text'})
                    if span is None:
                        player_settings[data_label] = ''
                    else:
                        player_settings[data_label] = span.find('a').get_text()
                except:
                    # TBD (To Be Decided) shows up as <abbr> not <a>. Made this try/except to future proof bc I'm lazy
                    player_settings[data_label] = ''
            else:
                player_settings[data_label] = data.get_text().strip()
        # Also for the weird table randomly inserted. Here's hoping the lazy approach doesn't bite me in 3 years time
        try:
            if (customize_settings.is_player_included_in_filters(player_settings)):
                list_of_cam_settings.append(player_settings)
        except:
            continue
    return list_of_cam_settings
