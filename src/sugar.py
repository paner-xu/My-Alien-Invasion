from abc import ABCMeta, abstractmethod


class Sugar(metaclass=ABCMeta):
    """a abstract class to manage three methods."""
    @abstractmethod
    def update(self):
        # a method to update position.
        pass

    @abstractmethod
    def check_collisions(self):
        # a method to check collisions of aliens with ship bullets laser guarder
        pass

    @abstractmethod
    def draw(self):
        # a method to draw on the screen
        pass
