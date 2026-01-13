from tennis.api_clients.api_tennis import call_api
from tennis.models import Player, Tournament, TournamentResult

def ingest_player_results_2025(player):
    history = call_api(
        "get_player_history",
        {
            "player_key": player.player_key,
            "date_start": "2025-01-01",
            "date_stop": "2025-12-31",
        },
    )

    for match in history.get("result", []):
        tournament, _ = Tournament.objects.update_or_create(
            tournament_key=match["tournament_key"],
            defaults={
                "name": match["tournament_name"],
            }
        )

        TournamentResult.objects.update_or_create(
            player=player,
            tournament=tournament,
            round=match["round"],
            defaults={"points": match["points"]},
        )
