# Up to date camera settings presets

A python program to scrape liquipedias camera settings page and create a file with the players settings you choose to include.

## Requirements and imports

Built on python3, and uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

## Setup and settings

the settingsForUpdate.py file will let you customize how the file is created. You can:

- Set constants (every preset created will have a set value, such as a preferred transition speed)
- Include team names (presets will show as "team_player" and are sorted by team)
- define what players you want to include (their names must match EXACTLY as it appears on the liquipedia page, so ctrl+c ctrl+v it)
  - You can also, if you really want, include every entry on that page. But then you'll have over 500 presets to scroll through, so I'd recommend just copying names to the list.
  - Not every player is present on that page, even though it seems like they should be. I can't do anything about that. Sorry.

## Usage

After editing the settings file to how you want it to work, just run the updateCamSettings.py file.
I'll try to clean this up later since I made this to use myself and recently decided I should upload it somewhere.
