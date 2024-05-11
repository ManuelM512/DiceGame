from dices import Dices
from strats import *
from simulations import *


def play_one_round():
    juan = juan_strategy()
    maria = maria_strategy(juan)
    winner = "Juan" if juan > maria else "María" if maria > juan else None
    return winner


def play_n_rounds(rounds_amount):
    rounds_victories = {"Juan": 0, "María": 0, "Empate": 0}
    for _ in range(rounds_amount):
        winner = play_one_round()
        if winner:
            rounds_victories[winner] += 1
        else:
            rounds_victories["Empate"] += 1
    return rounds_victories


def report_generator(rounds_victories):
    maria_r = rounds_victories["María"]
    juan_r = rounds_victories["Juan"]
    empate_r = rounds_victories["Empate"]
    
    rounds_amount = maria_r + juan_r + empate_r
    
    maria_frec = maria_r / rounds_amount
    juan_frec = juan_r / rounds_amount
    empate_frec = empate_r / rounds_amount
    
    victories_string = (
        f"Total de rondas: {rounds_amount}\n\n"
        + f"María ganó:      {maria_r}\n"
        + f"Juan ganó:       {juan_r}\n"
        + f"Empataron:       {empate_r}\n\n"
        + f"Frecuencia relativa de María:  {maria_frec}\n"
        + f"Frecuencia relativa de Juan:   {juan_frec}\n"
        + f"Frecuencia relativa de Empate: {empate_frec}\n\n"
        + f"Diferencia de frecuencia de María a Juan:"
        + f" {str(maria_frec-juan_frec)[0:6]}\n"
    )
    return victories_string


def play_n_matches(matches, rounds):
    stats = {"Juan": 0, "María": 0, "Empate": 0}
    for _ in range(matches):
        rounds_victories = play_n_rounds(rounds)
        juan_games = rounds_victories["Juan"]
        maria_games = rounds_victories["María"]
        round_winner = (
            "Juan"
            if juan_games > maria_games
            else "María" if maria_games > juan_games else None
        )
        if round_winner:
            stats[round_winner] += 1
        else:
            stats["Empate"] += 1

    return stats


def simulate_game():
    juan_simulation_sequence = []
    juan_points = juan_strategy(juan_simulation_sequence)
    maria_simulation_sequence = []
    maria_points = maria_strategy(juan_points, maria_simulation_sequence)
    juan_simulation(juan_simulation_sequence)
    print()
    maria_simulation(maria_simulation_sequence, juan_points)
    result = (
        "Juan"
        if juan_points > maria_points
        else "María" if maria_points > juan_points else "Empate"
    )
    return result


# Este correspondería a la parte 5 del trabajo
# rounds = play_n_rounds(1000))
# rounds = play_n_rounds(10000))
rounds = play_n_rounds(100000)
print(report_generator(rounds))

# n partidos de m rondas cada uno
# print(play_n_matches(10, 10000))

# Con este se puede simular una jugada
# simulate_game()
