import requests
import json

BASE = "http://localhost:8000/api/"
PLAYER_EP = f"{BASE}players"
CLAN_EP = f"{BASE}clans"
CLAN_MEMBER_EP = f"{BASE}clanmembers"

def get_clans():
    return requests.get(CLAN_EP).json()

if __name__ == "__main__":
    clans = get_clans()

    for clan in clans:
        print(f"Clan Name: {clan.get('name')}")
        print(f"Time Active: {clan.get('time_active')}")
        print(f"Tournament Win: {clan.get('tourney_won')}")