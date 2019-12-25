from abc import ABCMeta, abstractmethod


class Function(metaclass=ABCMeta):
    """a abstract class to manage three methods."""
    @abstractmethod
    def axis_update(self):
        # a method to move with the ship.
        pass

    @abstractmethod
    def check_collisions(self):
        # a method to check collisions of aliens with ship bullets laser guarder
        pass

    @abstractmethod
    def draw(self):
        # a method to draw on the screen
        pass

    @abstractmethod
    def update(self):
        # a method to update position.
        pass
