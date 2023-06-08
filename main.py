#!/bin/python3
import json
import requests
import sys

BASE_URL="https://api.speedrunslive.com/pastraces"

def urlBuilder(url, param, value):
    if '?' not in url:
        url += "?"
    else:
        url += "&"
    url += param + "=" + value
    return url

def download(url):
    res = requests.get(url)
    res.raise_for_status()
    return json.loads(res.text)

def get_races(player):
    x = 20
    past_races = []
    while True:
        url = urlBuilder(BASE_URL, "player", player)
        url = urlBuilder(url, "page", str(int(x/20)))
        page = download(url)
        for race in page['pastraces']:
            past_races.append(race)
        if page['count'] <= x:
            break
        x += 20
    return past_races

def main():
    if len(sys.argv) != 2:
        print("usage:", sys.argv[0], "[player name]", file=sys.stderr)
        return 1
    player = sys.argv[1]
    past_races = get_races(player)
    print(json.dumps(past_races))
    return 0

if __name__ == "__main__":
    sys.exit(main())
