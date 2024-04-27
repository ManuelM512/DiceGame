from dices import Dices
from strats import *

def play_n_matches(n):
    stats = {"Juan": 0, "María": 0}
    for j in range(10):
        rounds_victories = {"Juan": [0, 0], "María": [0, 0]}
        for i in range(n):
            juan = juan_strategy()
            maria = maria_strategy(juan)
            rounds_victories["María"][1] = rounds_victories["María"][1] + maria
            rounds_victories["Juan"][1] = rounds_victories["Juan"][1] + juan
            if juan > maria:
                rounds_victories["Juan"][0] = rounds_victories["Juan"][0] + 1
            elif maria == juan:
                v = 1
            else:
                rounds_victories["María"][0] = rounds_victories["María"][0] + 1
        print()
        if rounds_victories["Juan"][0] > rounds_victories["María"][0]:
            stats["Juan"] = stats["Juan"] + 1
            print("Ganó Juan")
        elif rounds_victories["María"][0] == rounds_victories["Juan"][0]:
            v = 1
        else:
            stats["María"] = stats["María"] + 1
            print("Ganó María")
        print("Juan:", rounds_victories["Juan"][1])
        print("María:", rounds_victories["María"][1])
    print(stats)

play_n_matches(1000)
