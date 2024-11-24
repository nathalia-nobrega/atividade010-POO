from breakout.HUD import HUD
from breakout.ball import Ball
from breakout.brick import Brick
from breakout.paddle import Paddle
from pong.position import Position
from pong.velocity import Velocity


class Game:
    def __init__(self):
        self.paddle = Paddle(Position(x=20, y=18))
        self.ball = Ball(Position(20, 10), Velocity(1, 1))
        self.bricks = [Brick(Position(x * 4, y)) for y in range(5) for x in range(10)]
        self.walls = {"width": 40, "height": 20}
        self.scoreboard = HUD()
        self.running = True

    def play_turn(self):
        print("\n--- Turno ---")
        self.ball.move()
        if self.ball.detect_collision(self.paddle, self.bricks, self.walls):
            self.scoreboard.update_score(10)
        self.print_game_state()

        if self.ball.position.y > self.walls["height"]:
            print("Game Over! A bola passou da raquete.")
            self.running = False

    def move_paddle(self, direction):
        self.paddle.move(direction)

    def print_game_state(self):
        print(f"Posição da bola: x={self.ball.position.x}, y={self.ball.position.y}")
        print(f"Posição da raquete: x={self.paddle.position.x}, y={self.paddle.position.y}")
        print(f"Pontuação: {self.scoreboard.player1_score}")
        print(f"Blocos restantes: {len([b for b in self.bricks if not b.destroyed])}")
