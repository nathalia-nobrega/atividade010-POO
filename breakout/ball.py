from pong.position import Position
from pong.velocity import Velocity

class Ball:
    def __init__(self, position: Position, velocity: Velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        self.position.x += self.velocity.dx
        self.position.y += self.velocity.dy
        print(f"A bola se moveu. Nova posição: x={self.position.x}, y={self.position.y}")

    def detect_collision(self, paddle, bricks, walls):
        # Collision with walls
        if self.position.x <= 0 or self.position.x >= walls["width"]:
            self.velocity.dx *= -1
            print("A bola colidiu com a parede de blocos..")

        if self.position.y <= 0:
            self.velocity.dy *= -1
            print("A bola colidiu com o teto.")

        # Collision with paddle
        if self.position.y == paddle.position.y and paddle.position.x <= self.position.x <= paddle.position.x + paddle.width:
            self.velocity.dy *= -1
            print("A bola colidiu com a raquete.")

        # Collision with bricks
        for brick in bricks:
            if not brick.destroyed and brick.position.x <= self.position.x <= brick.position.x + brick.width and brick.position.y == self.position.y:
                brick.destroyed = True
                self.velocity.dy *= -1
                print(f"A bola colidiu com um bloco em x={brick.position.x}, y={brick.position.y}. O bloco foi destruído.")
                return True

        return False

