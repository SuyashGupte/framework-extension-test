import json
data={}

data["workbench.colorTheme"] = "Default Dark+"
data["workbench.startupEditor"] = "none"

with open("/root/.local/share/code-server/User/settings.json", "w") as jsonFile:
    json.dump(data, jsonFile)
