import page_scraping
import customize_settings

print("Getting table from Liquipedia")
settings_list = page_scraping.get_table()

# Sort by team if team names are included
print("Sorting players")
if customize_settings.include_team_in_name:
    settings_list = sorted(settings_list, key=lambda k: k['Team'])
else:
    settings_list = sorted(settings_list, key=lambda k: k['Player'])

# Determine which filename to use
if customize_settings.replace_default_pro_settings:
    filename = "cameras_rlcs.data"
else:
    filename = "cameras_custom.cfg"

print("Writing to file")
f = open(filename, "w")
for player_settings in settings_list:
    if customize_settings.include_team_in_name and player_settings['Team'] != '':
        f.write(player_settings['Team'])
        f.write('_')
    f.write(player_settings["Player"].replace(" ","_"))
    f.write("\t")

    if customize_settings.perm_fov is not None:
        f.write(str(customize_settings.perm_fov))
    else:
        f.write(player_settings["FOV"])
    f.write("\t")

    if customize_settings.perm_height is not None:
        f.write(str(customize_settings.perm_height))
    else:
        f.write(player_settings["Height"])
    f.write("\t")

    if customize_settings.perm_angle is not None:
        f.write(str(customize_settings.perm_angle))
    else:
        f.write(player_settings["Angle"])
    f.write("\t")

    if customize_settings.perm_stiffness is not None:
        f.write(str(customize_settings.perm_stiffness))
    else:
        f.write(player_settings["Stiffness"])
    f.write("\t")

    if customize_settings.perm_transition_speed is not None:
        f.write(str(customize_settings.perm_transition_speed))
    else:
        f.write(player_settings["Transition speed"])
    f.write("\t")

    if customize_settings.perm_distance is not None:
        f.write(str(customize_settings.perm_distance))
    else:
        f.write(player_settings["Distance"])
    f.write("\t")

    if customize_settings.perm_swivel_speed is not None:
        f.write(str(customize_settings.perm_swivel_speed))
    else:
        f.write(player_settings["Swivel speed"])

    f.write("\n")
f.close()
print("Finished")
