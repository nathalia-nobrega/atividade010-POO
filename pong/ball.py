from pong.velocity import Velocity
from pong.wall import Wall
from pong.paddle import Paddle
from pong.position import Position

class Ball:
    def __init__(self, position: Position, velocity: Velocity):
        self.position = position
        self.velocity = velocity

    def move(self):
        self.position.x += self.velocity.dx
        self.position.y += self.velocity.dy

    def detect_collision_with_paddle(self, paddle: Paddle):
        # Verify collision
        if (paddle.position.x <= self.position.x <= paddle.position.x + paddle.width and
                paddle.position.y <= self.position.y <= paddle.position.y + paddle.height):
            self.velocity.dx *= -1
            print("Colisão com a raquete!")

    def detect_collision_with_walls(self, wall: Wall):

        if self.position.y <= wall.position.y:
            self.velocity.dy *= -1
            print("Colisão com a parede superior!")

        elif self.position.y >= wall.height - 1:
            self.velocity.dy *= -1
            print("Colisão com a parede inferior!")
