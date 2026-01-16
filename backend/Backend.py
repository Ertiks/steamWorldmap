from flask import Flask, jsonify
from flask_cors import CORS

from dotenv import load_dotenv

import requests, os

from routes.steam import steam_bp


#Charge les variables d'environnement :
load_dotenv()
STEAM_API_KEY = os.getenv("STEAM_KEY")

#A MODIFIER :
STEAM_ID_SATO = "76561198112866526"
STEAM_ID_INU = "76561198020830637"

STEAM_ID = STEAM_ID_SATO
#-----------

app = Flask(__name__)
CORS(app)

#Register des blueprints :
app.register_blueprint(steam_bp)

@app.route("/")
def testRoute():
    return "Backend fonctionnel"

# #-------------------------------
# @app.route("/games")
# def getSteamGames():

#     url = (
#         f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
#         f"?key={STEAM_API_KEY}"
#         f"&steamid={STEAM_ID}"
#         f"&include_appinfo=true"
#         f"&include_played_free_games=true"
#         f"&format=json"
#     )

#     response = requests.get(url)

#     if response.status_code != 200:
#         return jsonify({"error":"error with steam API"}), 500
    
#     data = response.json()

#     return jsonify(data["response"].get("game_count", -1))

