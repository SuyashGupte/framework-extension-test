with open("~/.local/share/code-server/User/settings.json", "r") as jsonFile:
    data = json.load(jsonFile)

data[ "workbench.colorTheme"] = "Default Dark+"

with open("~/.local/share/code-server/User/settings.json", "w") as jsonFile:
    json.dump(data, jsonFile)
