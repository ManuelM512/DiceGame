from dices import Dices
from strats import *


def play_n_matches(matches_per_game, games_amount):
    stats = {"Juan": 0, "María": 0}
    for _ in range(games_amount):
        rounds_victories = {"Juan": [0, 0], "María": [0, 0]}
        for _ in range(matches_per_game):
            juan = juan_strategy()
            maria = maria_strategy(juan)
            winner = "Juan" if juan > maria else "María" if maria > juan else None
            if winner:
                rounds_victories[winner][0] += 1
            else:
                rounds_victories["Juan"][0] += 1
                rounds_victories["María"][0] += 1
            rounds_victories["María"][1] = rounds_victories["María"][1] + maria
            rounds_victories["Juan"][1] = rounds_victories["Juan"][1] + juan

        juan_games = rounds_victories["Juan"][0]
        maria_games = rounds_victories["María"][0]
        round_winner = (
            "Juan"
            if juan_games > maria_games
            else "María" if maria_games > juan_games else None
        )
        if round_winner:
            stats[round_winner] += 1
        else:
            stats["Juan"] += 1
            stats["María"] += 1

    print(stats)


play_n_matches(10000, 100)
