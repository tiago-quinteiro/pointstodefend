import requests
import json
from datetime import datetime

API_KEY = "ee36445182630b05c7ddad4bdf6d345def590907e81f61fd2b76f60933fe50a0"  # Replace with your API-Tennis key
BASE_URL = "https://api.api-tennis.com/tennis/"

OUTPUT_FILE = "api_tennis_rankings_results_clean.json"
HEADERS = {"Accept": "application/json"}

def call_api(method, params=None):
    """Generic API-Tennis call."""
    query = {"method": method, "APIkey": API_KEY}
    if params:
        query.update(params)
    resp = requests.get(BASE_URL, params=query, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()

def fetch_top_100_atp():
    """Fetch top 100 ATP players."""
    standings = call_api("get_standings", {"event_type": "ATP"})
    if standings.get("success") != 1:
        raise Exception("Failed to fetch ATP standings")
    players = standings.get("result", [])[:100]
    top_players = []
    for p in players:
        top_players.append({
            "rank": int(p.get("place")),
            "player_name": p.get("player"),
            "player_key": p.get("player_key"),
            "points": int(p.get("points")),
            "nationality": p.get("country"),
            "results": []  # Will be filled later
        })
    return top_players

def fetch_player_results(player_key, year=2025):
    """Fetch all matches for a player in a specific year using get_fixtures and simplify the info."""
    date_start = f"{year}-01-01"
    date_stop = f"{year}-12-31"
    fixtures = call_api(
        "get_fixtures",
        {"player_key": player_key, "date_start": date_start, "date_stop": date_stop}
    )
    if fixtures.get("success") != 1:
        return []

    simplified_results = []
    for f in fixtures.get("result", []):
        simplified_results.append({
            "tournament_key": f.get("tournament_key"),
            "tournament_name": f.get("tournament_name"),
            "tournament_season": f.get("tournament_season"),
            "tournament_round": f.get("tournament_round"),
            "event_type": f.get("event_type_type"),
            "event_date": f.get("event_date"),
            "event_time": f.get("event_time"),
            "first_player": f.get("event_first_player"),
            "first_player_key": f.get("first_player_key"),
            "second_player": f.get("event_second_player"),
            "second_player_key": f.get("second_player_key"),
            "final_result": f.get("event_final_result"),
            "winner": f.get("event_winner")
        })
    return simplified_results

def main():
    print("Fetching top 100 ATP players...")
    players = fetch_top_100_atp()

    print("Fetching 2025 results for each player...")
    for idx, player in enumerate(players, start=1):
        print(f"[{idx}/100] {player['player_name']}...")
        results = fetch_player_results(player["player_key"], year=2025)
        player["results"] = results

    # Save everything to JSON
    data_output = {
        "generated_at": datetime.utcnow().isoformat(),
        "players": players
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data_output, f, indent=2, ensure_ascii=False)

    print(f"Saved top 100 ATP players + 2025 simplified results to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
