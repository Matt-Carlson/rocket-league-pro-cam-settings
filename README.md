# Up to date Camera Settings Presets

A python program to scrape [Liquipedia camera settings page](https://liquipedia.net/rocketleague/List_of_player_camera_settings) and create a file with the players settings you choose to include.

### [Requirements and Imports](#requirements-and-imports)

### [Usage](#usage)

### [Setup and Settings](#setup-and-settings)

## Requirements and Imports

- [Python3](https://www.python.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- Requests python package

## Usage

Make sure you set up the [customize_settings.py](https://github.com/Matt-Carlson/rocket-league-pro-cam-settings/blob/main/customize_settings.py) file. I have my own there but you probably don't want the same permanent settings I do.
The most important thing to check are those permanent settings at the top. Below that is the part you care about more.

```python
# If you want to ignore certain settings, then manually set the settings you want here
# To record the pros settings leave it as 'None'
# The format the default file has for each setting is in the comment on that line
    # i.e. permFOV can be 110, 095, ...
perm_fov = None              # 000
perm_distance = None         # 000.0
perm_height = None           # 000
perm_angle = None            # -0
perm_stiffness = None        # 0.0
perm_swivel_speed = 10.00      # 0.00
perm_transition_speed = 2.00  # 1.00
```

As it's listed here the swivel speed will always be 10 and transition speed 2, for every preset, regardless of what it says on Liquipedia.
This is a convience if, like me, you have some settings you don't want to change between your presets.

After editing the settings file, just run the updateCamSettings.py file as `py create_camera_preset_file.py`.
It will create a file in the same directory by the name `cameras_rlcs.data` or `cameras_custom.cfg`. (The first option when you move it to your bakkesmod directory will overwrite the default rlcs settings that appear by default, and when it updates. BakkesMod will overwrite your stuff when it updates on this. The second doesn't overwrite those, and they appear first, so just use that tbh.)

Take that file, and place it into your `bakkesmod\data` directory (there should already be files by those names there. If you aren't overwriting, it's probably the wrong place)
If you don't know where it is, open bakkesmod, and click file -> open bakkesmod folder. Then navigate into the data folder.

## Setup and Settings

the [customize_settings.py](https://github.com/Matt-Carlson/rocket-league-pro-cam-settings/blob/main/customize_settings.py) file will let you customize how the file is created. You can:

- Set constants (every preset created will have a set value, such as a preferred transition speed)
- Include team names in the preset name (presets will show as "team_playername" instead of "playername" and are sorted by team)
- Define what players or teams to include (the player name or team abbreviation must match EXACTLY asit appears on the Liquipedia page, so ctrl+c ctrl+v it)
  - Not every player is present on that page, even though it seems like they should be. I can't do anything about that.
  - The settings may also not be very recent. Lots of pros have a habbit of changing settings every 5 games. If you update Liquipedia, then so will this.

### Detailed info on all settings

```python
# If you want to ignore certain settings, then manually set the settings you want here
# To record the pros settings leave it as 'None'
# The format the default file has for each setting is in the comment on that line
    # i.e. permFOV can be 110, 095, ...
perm_fov = None              # 000
perm_distance = None         # 000.0
perm_height = None           # 000
perm_angle = None            # -0
perm_stiffness = None        # 0.0
perm_swivel_speed = 10.00      # 0.00
perm_transition_speed = 2.00  # 1.00
```

These are the permanent settings. If, like me, you have some settings you don't want to change between your presets then setting them here will overwrite what the pros have.
By default these are the settings, so the transition speed will always be 2, and swivel speed always 10, and all others will vary according to Liquipedia's record. Set the swivel / transition speed to "None" to capture pro settings.
The default format for each is displayed in a comment on the same line. I doubt it's necessary but I copied it over anyway.

```python
# Use true to place the team abbreviation before player name in the menu
# It will be sorted by teams if you do this
include_team_in_name = True
```

This only affects the display of the presets in your settings menu. Making this true means that players will show up with their team name first, and the presets will be ordered by team alphabetically.
so bds members show as `BDS_Extra` `BDS_MaRc_By_8.` `BDS_M0nkey_M00n` when set to true, and `Extra` `MaRc_By_8.` `M0nkey_M00n` when false. (Dating when I made this. If it didn't already have a date attached.)
If a player doesn't belong to any team, then they show up by just their name.

```python
# Use true to replace the file that by default has some pro settings.
# False will instead name the file for the custom file that's empty by default
replace_default_pro_settings = True
```

When true, the file created will be `cameras_rlcs.data` and if you copy it over will overwrite the default rlcs presets that come with bakkesmod. If you have both the filters below as `False`, then the created file will be empty, and you won't see any presets if you move over the empty file.
This file is also updated when bakkesmod updates, so you may find that your presets change, this is why.
When false, the file created will be `cameras_custom.cfg` and won't overwrite the default presets. They will show above the defaults.

```python
# Set to true to filter by team name. This means all players under the abbreviations in included_teams will be added
filter_by_team = True

# Set to true to filter by individual players. This will stack with the above filter for teams to include only players on those teams AND in included_players
filter_by_player = False
```

These booleans set what you filter by. You must have at least one set to `True` for any presets to show up.
`filter_by_team` uses the `included_teams` list below, and `filter_by_player` the `included_players` list.
They do stack, so you must have both teams and players on those teams in the lists to get any results if both are set to true.
_Since there are so many settings listed I have chosen to not allow creating a file with all of them. If you really want 500 presets to scroll through you can just comment out the line where I check these lists._

```python
# Team abbreviations as listed on Liquipedia to include.
# Make sure that they match how it appears on liquipedia (all caps too)
# you MUST have filter_by_team set to true for this to matter. This lets you turn it on/off without erasing/commenting out this list
included_teams = [
    'BDS',
    'VIT',
    'TB'
]

# Player names as listed on liquipedia to include. Keeps your list from being
# 20 years long. If the names aren't an EXACT match (including the '.'s), they won't show up
# you MUST have filter_by_player set to true for this to matter. This lets you turn it on/off without erasing/commenting out this list
included_players = [
    'Extra',
    'M0nkey M00n',
    'MaRc_By_8.',
]
```

These lists are used to declare what teams or players you want to include.
The `included_teams` should match the abbreviations that are on Liquipedia. It's case-sensitive so caps-lock it. Or copy/paste.
The `included_players` are also case-sensitive and must match exactly the player names on Liquipedia. (See that '.' on MaRc_By_8.? that needs to be there. Again, copy/paste it from the [Table I use](https://liquipedia.net/rocketleague/List_of_player_camera_settings))
