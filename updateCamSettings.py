import pageScraping
import settingsForUpdate

settingsList = pageScraping.getTable()
# print(settingsList)


if settingsForUpdate.includeTeamInName:
    settingsList.sort(key=lambda camSettingsProfile: camSettingsProfile.team)

f = open("cameras_rlcs.data", "w")
for value in settingsList:
    # print(value)
    f.write(value.__str__())
    f.write("\n")
f.close()
print("Finished.")
