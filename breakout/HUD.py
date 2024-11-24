class HUD:
    def __init__(self):
        self.player1_score = 0
        self.lives = 3

    def update_score(self, points: int):
        self.player1_score += points

    def display_hud(self):
        print(f"Placar: Jogador 1 = {self.player1_score}\tVidas: {self.lives}")