from random import choices, randint

dice_faces = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]


class Dices:
    # Preferí utilizar esta forma de incializar los dados porque me parecía más puritano que,
    # salieran en "una sola tirada" que hacer dos líneas de randints :)
    def __init__(self):
        self.first_dice, self.second_dice = choices(dice_faces, k=2)

    def get_dices(self):
        return [self.first_dice, self.second_dice]

    def rethrow_one(self):
        if self.first_dice == 4:
            self.second_dice = randint(1, 6)
        else:
            self.first_dice = randint(1, 6)

    def rethrow_both(self):
        self.first_dice, self.second_dice = choices(dice_faces, k=2)
