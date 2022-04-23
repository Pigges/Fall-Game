import pygame, random, config

# TODO: Create surface and make visible
# TODO: Make the Wall move upwards

class Wall(pygame.sprite.Sprite):
    """The Wall class
    \nNeeds 'game' (the parent class)"""

    def __init__(self, game: object) -> None:
        self.game = game # Assign the game(parent class) to self.game for later use
        self._layer = config.WALL_LAYER
        self.groups = self.game.walls, self.game.all_sprites # Assigns the groups
        pygame.sprite.Sprite.__init__(self, self.groups) # Initialize the sprite

        self.x = random.randint(0, 100-config.WALL_GAP) # self.x: Will be where the gap starts
        self.y = pygame.display.get_window_size()[0] # self.y: Will start just under the window
        print(self.x)
        print(self.y)

    def update(self):
        pass