from pong.paddle import Paddle
from pong.ball import Ball
from pong.velocity import Velocity
from pong.position import Position
from pong.scoreboard import Scoreboard
from pong.wall import Wall

class Game:
    def __init__(self):
        self.wall = Wall(0, 0, width=40, height=20)

        self.ball = Ball(Position(self.wall.width // 2, self.wall.height // 2), Velocity(1, 1))
        self.player1 = Paddle(Position(1, self.wall.height // 2 - 3), width=1, height=6, speed=1)
        self.player2 = Paddle(Position(self.wall.width - 2, self.wall.height // 2 - 3), width=1, height=6, speed=1)
        self.scoreboard = Scoreboard()

        # state of the game
        self.running = True

    def play_turn(self):
        print("\n--- Turno ---")

        self.ball.move()

        # collision
        self.ball.detect_collision_with_walls(self.wall)
        self.ball.detect_collision_with_paddle(self.player1)
        self.ball.detect_collision_with_paddle(self.player2)

        # score
        if self.ball.position.x <= 0:  # Ponto para o Jogador 2
            self.scoreboard.update_score(player=2)
            print("Ponto para o Jogador 2!")
            self.reset_ball()
        elif self.ball.position.x >= self.wall.width:  # Ponto para o Jogador 1
            self.scoreboard.update_score(player=1)
            print("Ponto para o Jogador 1!")
            self.reset_ball()

        # victory condition
        if self.scoreboard.player1_score >= 10:
            print("Jogador 1 venceu!")
            self.running = False
        elif self.scoreboard.player2_score >= 10:
            print("Jogador 2 venceu!")
            self.running = False

        self.print_game_state()

    def move_paddle(self, player: int, direction: str):
        # select the correct paddle
        paddle = self.player1 if player == 1 else self.player2

        # paddle movement
        if direction == "acima":
            if paddle.position.y > 0:
                paddle.move_up()
            else:
                print(f"Jogador {player}: Raquete no limite superior!")
        elif direction == "abaixo":
            if paddle.position.y + paddle.height < self.wall.height:
                paddle.move_down(self.wall.height)
            else:
                print(f"Jogador {player}: Raquete no limite inferior!")
        else:
            print("Direção inválida. Use 'acima' ou 'abaixo'.")

    def reset_ball(self):
        self.ball.position = Position(self.wall.width // 2, self.wall.height // 2)
        self.ball.velocity = Velocity(1, 1)

    def print_game_state(self):
        print("\n=== Estado do Jogo ===")
        print(f"Bola: (x={self.ball.position.x}, y={self.ball.position.y})")
        print(f"Jogador 1: Posição y={self.player1.position.y}, Placar={self.scoreboard.player1_score}")
        print(f"Jogador 2: Posição y={self.player2.position.y}, Placar={self.scoreboard.player2_score}")
        print("=======================")
