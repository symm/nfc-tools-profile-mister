#!/usr/bin/env python3

import json

dirlisting = open('arcade.txt', 'r')
Lines = dirlisting.readlines()
 
profile = []

for line in Lines:
    corename = line.strip().replace(".mra", "")
    path = "_Arcade/" + line.strip()
    profile.append({
        "tag.profile.name":  corename,
        "tag.profile.date": "20230804T225330",
        "tag.profile.length": 1,
        "tag.profile.size": len(path) + 7,
        "tag.profile.data": [
            {
                "tag.profile.fields": {
                    "field1": path
                },
                "tag.profile.config": {
                    "requestType": "1",
                    "itemRecordExtra": "",
                    "itemDescription": path,
                    "itemRecord": path,
                }
            }
        ]
        })
print(json.dumps(profile))