class Characters:
    def __init__(self, player, encounter_size, turn, initiave):
        self.name = player[0]
        self.hp = player[1]
        self.initiative = initiave
        self.turn = turn
        self.encounter_size = encounter_size
        self.reaction = False
        self.dead = False

    def hp_counter(self, change):
        self.hp += change
        if self.hp <= 0:
            self.dead = True

    def turn_counter(self):
        self.turn += 1


class Enemies:
    def __init__(self, enemies):
        self.encounter_size = int(enemies[0][0]) + int(enemies[0][1])
        self.initiave = None

    def enemies(self, enemies):
        enemy = []
        for i in range(self.encounter_size):
            name = enemies[i][0]
            dex_mod = enemies[i][1]
            enemy.append((name, dex_mod))


def compare_initiave():
    pass
