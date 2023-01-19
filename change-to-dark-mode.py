data={}

data["workbench.colorTheme"] = "Default Dark+"

with open("/root/.local/share/code-server/User/settings.json", "w") as jsonFile:
    json.dump(data, jsonFile)
