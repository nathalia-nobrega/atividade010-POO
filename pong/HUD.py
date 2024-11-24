class HUD:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0

    def update_score(self, player: int):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1

    def display_score(self):
        print(f"Placar: Jogador 1 = {self.player1_score}, Jogador 2 = {self.player2_score}")