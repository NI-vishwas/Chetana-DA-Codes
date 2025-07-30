#!/usr/bin/env python3

import json

try:
    with open('data.json') as fh:
        json_str = fh.read()
        data = json.loads(json_str)
        print(data)
except FileNotFoundError:
    print("File not found")
