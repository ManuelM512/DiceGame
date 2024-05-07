def juan_simulation(sequence):
    points = (
        sequence[0][1]
        if sequence[0][0] == 4
        else sequence[0][0] if sequence[0][1] == 4 else 0
    )
    print("Juan:\nTiro mis dados y saco...")
    if len(sequence) == 1:
        print(f"Saqué un 4 y un {points}, esos son {points} puntos, paro aquí")
    elif points == 0:
        print(
            f"Tiré {sequence[0][0]} y {sequence[0][1]}, esos son 0 puntos, volveré a tirar ambos"
        )
        points = (
            sequence[1][1]
            if sequence[1][0] == 4
            else sequence[1][0] if sequence[1][1] == 4 else 0
        )
        print(
            f"Ahora tiré {sequence[1][0]} y {sequence[1][1]}, esos son {points} puntos"
        )
    else:
        print(
            f"Tiré {sequence[0][0]} y {sequence[0][1]}, esos son {points} puntos,"
            + " como no son más de 3 puntos, volveré a tirar un dado"
        )
        rethrowed_dice = sequence[1][0] if sequence[1][1] == 4 else sequence[1][0]
        print(f"Ahora tiré {rethrowed_dice}, esos son {rethrowed_dice} puntos")


def maria_simulation(sequence, juan_points):
    points = (
        sequence[0][1]
        if sequence[0][0] == 4
        else sequence[0][0] if sequence[0][1] == 4 else 0
    )
    print(f"María:\nTiré {sequence[0][0]} y {sequence[0][1]}, esos son {points} puntos")
    if len(sequence) == 1:
        if points == juan_points:
            if points == 6:
                print("No hay forma de ganarle, mejor freno acá")
            else:
                print(
                    "Es difícil que le gane a Juan si vuelvo a tirar solo este dado, mejor freno aquí"
                )
        else:
            print(f"Hice más puntos que Juan")
    else:
        if points == 0:
            print("Volveré a tirar ambos")
            points = (
                sequence[1][1]
                if sequence[1][0] == 4
                else sequence[1][0] if sequence[1][1] == 4 else 0
            )
            print(
                f"Ahora saqué {sequence[1][0]} y {sequence[1][1]}, esos son {points} puntos"
            )
        else:
            if points < juan_points:
                print(
                    f"Saqué un 4, pero no supero los {juan_points} puntos de Juan, debo volver a tirar"
                )
            else:
                if points == juan_points:
                    print(
                        f"Empaté con Juan en {points} puntos,"
                        + " volveré a tirar porque tengo mejores casos favorables que no"
                    )
            rethrowed_dice = sequence[1][0] if sequence[1][1] == 4 else sequence[1][1]
            print(f"Ahora tiré {rethrowed_dice}, esos son {rethrowed_dice} puntos")
    if len(sequence) == 1:
        points = (
            sequence[0][1]
            if sequence[0][0] == 4
            else sequence[0][0] if sequence[0][1] == 4 else 0
        )
    else:
        points = (
            sequence[1][1]
            if sequence[1][0] == 4
            else sequence[1][0] if sequence[1][1] == 4 else 0
        )
    if points > juan_points:
        print("Le gané a Juan!")
    elif points == juan_points:
        print("Empaté con Juan.")
    else:
        print("Perdí con Juan...")
    print(f"Con {points} a {juan_points} puntos")
    # TODO: Cambiarlo para que reciba los puntos de Juan, y que diga como le fue si gano o no, y que las condiciones sean en base a cuantos turnos
