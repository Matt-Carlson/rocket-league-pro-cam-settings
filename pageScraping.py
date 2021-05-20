import requests
from bs4 import BeautifulSoup
import settingsForUpdate


class camSettingsProfile:
    def __init__(self, playerName, team, fov, height, angle, stiffness, transitionSpeed, distance, swivelSpeed):
        self.playerName = playerName
        if team is None:
            self.team = ""
        else:
            self.team = team

        if settingsForUpdate.permFov is None:
            self.fov = fov
        else:
            self.fov = settingsForUpdate.permFov

        if settingsForUpdate.permHeight is None:
            self.height = height
        else:
            self.height = settingsForUpdate.permHeight

        if settingsForUpdate.permAngle is None:
            self.angle = angle
        else:
            self.angle = settingsForUpdate.permAngle

        if settingsForUpdate.permStiffness is None:
            self.stiffness = stiffness
        else:
            self.stiffness = settingsForUpdate.permStiffness

        if settingsForUpdate.permTransitionSpeed is None:
            self.transitionSpeed = transitionSpeed
        else:
            self.transitionSpeed = settingsForUpdate.permTransitionSpeed

        if settingsForUpdate.permDistance is None:
            self.distance = distance
        else:
            self.distance = settingsForUpdate.permDistance

        if settingsForUpdate.permSwivelSpeed is None:
            self.swivelSpeed = swivelSpeed
        else:
            self.swivelSpeed = settingsForUpdate.permSwivelSpeed

    def __str__(self):
        if settingsForUpdate.includeTeamInName and self.team is not None:
            return "{0}_{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(self.team, self.playerName, self.fov, self.height, self.angle, self.stiffness, self.transitionSpeed, self.distance, self.swivelSpeed)
        return "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(self.playerName, self.fov, self.height, self.angle, self.stiffness, self.transitionSpeed, self.distance, self.swivelSpeed)


def getTable():
    """
Scrape the table from liquipedia, and return list of only desired player cam settings
"""
    page = requests.get(
        "https://liquipedia.net/rocketleague/List_of_player_camera_settings")
    soup = BeautifulSoup(page.text, 'html.parser')

    camSettingsTable = soup.find(
        "table", {"class": "rl-responsive-table-sortable"}).find_all('tr')

    # First row is the header, just skip that.
    data = []
    for row in camSettingsTable[1:]:
        line = row.find_all('td')
        # print(line[0].contents[1].text.strip())
        name = line[0].contents[1].text.strip()

        # continue only if required
        if settingsForUpdate.recordAllSettings or name in settingsForUpdate.includedPlayers:
            # remove whitespace, required for bakkes
            name = name.replace(" ", "")
            # Not every player has a team
            try:
                team = line[1].contents[0].contents[2].string
            except:
                team = None
            camShake = 2
            fov = line[3].contents[0].string.strip('\n')
            height = line[4].contents[0].string.strip('\n')
            angle = line[5].contents[0].string.strip('\n')
            distance = line[6].contents[0].string.strip('\n')
            stiff = line[7].contents[0].string.strip('\n')
            swivel = line[8].contents[0].string.strip('\n')
            transition = line[9].contents[0].string.strip('\n')
            settings = camSettingsProfile(
                name, team, fov, height, angle, stiff, transition, distance, swivel)
            # print(settings)
            data.append(settings)
    return data
