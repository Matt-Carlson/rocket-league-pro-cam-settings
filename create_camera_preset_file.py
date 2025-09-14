import page_scraping
import customize_settings

print("Getting table from Liquipedia")
settings_list = page_scraping.get_table()

# Sort by team if team names are included
print("Sorting players")
if customize_settings.include_team_in_name:
    settings_list = sorted(settings_list, key=lambda k: k["Team"])
else:
    settings_list = sorted(settings_list, key=lambda k: k["Player"])

# Determine which filename to use
if customize_settings.replace_default_pro_settings:
    filename = "cameras_rlcs.data"
else:
    filename = "cameras_custom.cfg"

print("Writing to file")
f = open(filename, "w")
for player_settings in settings_list:
    if customize_settings.include_team_in_name and player_settings["Team"] != "":
        f.write(player_settings["Team"])
        f.write("_")
    f.write(player_settings["Player"].replace(" ", "_"))
    f.write("\t")

    (
        f.write(player_settings["FOV"])
        if customize_settings.perm_fov is None
        else f.write(str(customize_settings.perm_fov))
    )
    f.write("\t")

    (
        f.write(player_settings["Height"])
        if customize_settings.perm_height is None
        else f.write(str(customize_settings.perm_height))
    )
    f.write("\t")

    (
        f.write(player_settings["Angle"])
        if customize_settings.perm_angle is None
        else f.write(str(customize_settings.perm_angle))
    )
    f.write("\t")

    (
        f.write(player_settings["Stiffness"])
        if customize_settings.perm_stiffness is None
        else f.write(str(customize_settings.perm_stiffness))
    )
    f.write("\t")

    (
        f.write(player_settings["Transition speed"])
        if customize_settings.perm_transition_speed is None
        else f.write(str(customize_settings.perm_transition_speed))
    )
    f.write("\t")

    (
        f.write(player_settings["Distance"])
        if customize_settings.perm_distance is None
        else f.write(str(customize_settings.perm_distance))
    )
    f.write("\t")

    (
        f.write(player_settings["Swivel speed"])
        if customize_settings.perm_swivel_speed is None
        else f.write(str(customize_settings.perm_swivel_speed))
    )

    f.write("\n")
f.close()
print("Finished")
