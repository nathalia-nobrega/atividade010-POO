from breakout.ball import Ball
from breakout.brick import Brick
from breakout.paddle import Paddle


class Game:
    def __init__(self):
        self.paddle = Paddle(x=20, y=18)
        self.ball = Ball()
        self.bricks = [Brick(x * 4, y) for y in range(5) for x in range(10)]
        self.walls = {"width": 40, "height": 20}
        self.score = 0
        self.running = True

    def play_turn(self):
        print("\n--- Turno ---")
        self.ball.move()
        if self.ball.detect_collision(self.paddle, self.bricks, self.walls):
            self.score += 10

        self.print_game_state()

        if self.ball.y > self.walls["height"]:
            print("Game Over! A bola passou da raquete.")
            self.running = False

    def move_paddle(self, direction):
        self.paddle.move(direction)

    def print_game_state(self):
        print(f"Posição da bola: x={self.ball.x}, y={self.ball.y}")
        print(f"Posição da raquete: x={self.paddle.x}, y={self.paddle.y}")
        print(f"Pontuação: {self.score}")
        print(f"Blocos restantes: {len([b for b in self.bricks if not b.destroyed])}")
