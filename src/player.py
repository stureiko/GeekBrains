class Player:
    """
    Класс игрока
    """
    health = 10
    max_health = 10
    default_damage = 10
    position = [0, 0]

    def was_hit(self, hamster_force):
        # self.health -= random.choice(range(hamster_force + 1))
        self.health -= hamster_force

    def wait(self):
        if not self.health == self.max_health:
            self.health += 1
            print(f'I restored health, it\'s = {self.health}')
