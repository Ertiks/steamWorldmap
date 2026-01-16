from flask import Blueprint, jsonify
from config import STEAM_API_KEY, STEAM_ID_DEBUG

from services.steam_service import get_profile


#blueprint : 
steam_bp = Blueprint("steam", __name__, url_prefix="/steam")


@steam_bp.get("/profile")
def profile():
    return jsonify(get_profile(STEAM_API_KEY, STEAM_ID_DEBUG))

@steam_bp.get("/games")
def steamGames():
    return jsonify()

