from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

STEAM_API_KEY = "---"
STEAM_ID_SATO = "76561198112866526"
STEAM_ID_INU = "76561198020830637"

STEAM_ID = STEAM_ID_SATO

@app.route("/")
def testRoute():
    return "Backend fonctionnel"

#-------------------------------
@app.route("/profile")
def getUserProfile():
    url = (
        f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
        f"?key={STEAM_API_KEY}"
        f"&steamids={STEAM_ID}"
    )

    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error":"error with steam API"}), 500
    
    data = response.json()
    player = data["response"]["player"][0]

    return jsonify({
        "name": player["personaname"],
        "avatar": player["avatar"],
        "profile_url": player["profileurl"]
    })
    
#-------------------------------
@app.route("/games")
def getSteamGames():

    url = (
        f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
        f"?key={STEAM_API_KEY}"
        f"&steamid={STEAM_ID}"
        f"&include_appinfo=true"
        f"&include_played_free_games=true"
        f"&format=json"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error":"error with steam API"}), 500
    
    data = response.json()

    return jsonify(data["response"].get("game_count", -1))

