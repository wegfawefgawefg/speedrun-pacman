from vec2 import Vec2

class Entity:
    def __init__(self, position):
        self.position = position
        self.direction = Vec2(1, 0)
        self.move_delay = 10
        self.time_since_last_move = 0

    def move(self, dt, map, entities):
        if self.time_since_last_move > self.move_delay:
            # check that you can move on map
            # check that no entities are there
                # move there if you can
            self.time_since_last_move = 0
        else:
            self.time_since_last_move += dt

    def draw(graphics):
        raise NotImplementedError

class Pacman(Entity):
    def __init__(self, position):
        super.__init__(self, position)

    def draw(graphics):
        

