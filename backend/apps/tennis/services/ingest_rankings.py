from tennis.api_clients.api_tennis import call_api
from tennis.models import Player

def ingest_top_100_atp():
    data = call_api("get_standings", {"event_type": "ATP", "limit": 100})
    for p in data.get("result", []):
        Player.objects.update_or_create(
            player_key=p["player_key"],
            defaults={
                "name": p["player_name"],
                "ranking": p["rank"],
                "points": p["points"],
                "nationality": p.get("country_code"),
            }
        )
