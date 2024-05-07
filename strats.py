from dices import Dices


def points_calculator(dices):
    dices_pair = dices.get_dices()
    if 4 in dices_pair:
        return dices_pair[0] if dices_pair[1] == 4 else dices_pair[1]

    return 0


def maria_strategy(juan_points, simulation_sequence=[]):
    maria_dices = Dices()
    simulation_sequence.append(maria_dices.get_dices())
    maria_points = points_calculator(maria_dices)
    # Hace 0 pts, la única posibilidad es volver a tirar ambos y devuelve el resultado
    if maria_points == 0:
        maria_dices.rethrow_both()
        simulation_sequence.append(maria_dices.get_dices())
        maria_points = points_calculator(maria_dices)
        return maria_points
    # María hizo al menos 1 punto, en su primer tirada, para todos los casos siguientes
    # Hizo más puntos, frena ahí
    if maria_points > juan_points:
        return maria_points
    if maria_points < juan_points or juan_points <= 3:
        maria_dices.rethrow_one()
        simulation_sequence.append(maria_dices.get_dices())
        maria_points = points_calculator(maria_dices)
    return maria_points


def juan_strategy(simulation_sequence=[]):
    juan_dices = Dices()
    simulation_sequence.append(juan_dices.get_dices())
    juan_points = points_calculator(juan_dices)
    if juan_points <= 3:
        juan_dices.rethrow_one() if juan_points > 0 else juan_dices.rethrow_both()
        simulation_sequence.append(juan_dices.get_dices())
        juan_points = points_calculator(juan_dices)

    return juan_points
