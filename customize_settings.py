
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

# Use true to place the team abbreviation before player name in the menu
# It will be sorted by teams if you do this
include_team_in_name = True

# Use true to replace the file that by default has some pro settings.
# False will instead name the file for the custom file that's empty by default
replace_default_pro_settings = False

# Set to true to filter by team name. This means all players under the abbreviations in included_teams will be added
filter_by_team = True

# Set to true to filter by individual players. This will stack with the above filter for teams to include only players on those teams AND in included_players
filter_by_player = False

# Team abbreviations as listed on Liquipedia to include.
# Make sure that they match how it appears on liquipedia (all caps too)
# you MUST have filter_by_team set to true for this to matter. This lets you turn it on/off without erasing/commenting out this list
included_teams = [
    'KC',
    'VIT',
    'DIG',
    'NIP',
    'GK',

    'NRG',
    'TU',
    'SSG',
    'GENG',
    'SR',
    
    'TSM',
    'WC',

    'VP',

    'FUR',
    'TS',

    'FLCN',
    'TWIS'
]

# Player names as listed on liquipedia to include. Keeps your list from being
# 20 years long. If the names aren't an EXACT match (including the '.'s), they won't show up
# you MUST have filter_by_player set to true for this to matter. This lets you turn it on/off without erasing/commenting out this list
included_players = [
    'Extra',
    'M0nkey M00n',
    'MaRc_By_8.',
    'ApparentlyJack',
    'Joreuz',
    'Metsanauris',
    'RelatingWave',
    'JKnaps',
    'Rizzo',
    'BeastMode',
    'Dappur',
    'Memory',
    'GarrettG',
    'jstn.',
    'SquishyMuffinz',
    'Atomic',
    'mist',
    'AztraL',
    'Chausette45',
    'Ferra',
    'Gyro.',
    'majicbear',
    'firstkiller',
    'Taroco',
    'CJCJ',
    'Breezi',
    'hibbs',
    'Scrub Killa',
    'Roll Dizz',
    'Shock',
    'oKhaliD',
    'Arsenal',
    'retals',
    'Sypical',
    'Speed',
    'archie',
    'Kassio',
    'AtomiK',
    'Alpha54',
    'Fairy Peak!',
    'Kaydop'
]

def is_player_included_in_filters(player_settings):
    """
        Determines if the given player_settings dictionary should be included according to the settings in customize_settings.py
    """
    if filter_by_team and player_settings['Team'] not in included_teams:
        return False
    if filter_by_player and player_settings['Player'] not in included_players:
        return False
    return True