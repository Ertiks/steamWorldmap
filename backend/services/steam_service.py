from errors import SteamError

import requests

#logique métier

def get_profile(api_key, steam_id):
    

    if not api_key:
        raise ValueError("no API key")
    
    url = (
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
        f"?key={api_key}"
        f"&steamids={steam_id}"
    )
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise SteamError("error Steam API")
    
    data = response.json()

    players = data.get("response", {}).get("players", [])
    
    player = players[0]

    return{
        "steam_id": steam_id,
        "name": player.get("personaname"),
        "avatar": player.get("avatar"),
        "avatarmedium": player.get("avatarmedium"),
    }
    
