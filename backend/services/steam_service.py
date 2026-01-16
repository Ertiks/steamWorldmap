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
        "avatarfull": player.get("avatarfull"),
    }


def get_steam_games(api_key, steam_id):

    url = (
        f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        f"?key={api_key}"
        f"&steamid=steam_id{steam_id}"
        f"&include_appinfo=true"
        f"&include_played_free_games=true"
        f"&format=json"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except:
        raise SteamError("error Steam API")
    
    data = response.json()

    return jsonify(data["response"].get("game_count", -1))
    
