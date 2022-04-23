import pygame, config

class Player(pygame.sprite.Sprite):
    """The Player class
    \nNeeds 'game' (the parent class)"""

    def __init__(self, game: object) -> None:
        self.game = game # Assign the game(parent class) to self.game for later use
        self._layer = config.WALL_LAYER
        self.groups = self.game.playerG, self.game.all_sprites # Assigns the groups
        pygame.sprite.Sprite.__init__(self, self.groups) # Initialize the sprite


    def update(self):
        pass