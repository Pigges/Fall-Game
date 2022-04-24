import pygame, random, config

class Wall(pygame.sprite.Sprite):
    """The Wall class
    \nNeeds 'game' (the parent class)"""

    def __init__(self, game: object) -> None:
        self.game = game # Assign the game(parent class) to self.game for later use
        self._layer = config.WALL_LAYER
        self.groups = self.game.walls, self.game.all_sprites # Assigns the groups
        pygame.sprite.Sprite.__init__(self, self.groups) # Initialize the sprite
        self.screen_size = pygame.display.get_window_size() # Fetching the screen size [list] usage: x: [0], y: [1]
        self.hasChild = False # Remember if it is the latest wall or not

        self.gapStart = random.randint(0, 100-config.WALL_GAP)/100 # self.gapStart: Will be where the gap starts
        self.y = self.screen_size[1] # self.y: Will start just under the window

        self.createSprite() # Setting up and creating the sprite

        self.speed = 1
        

    def createSprite(self):
        part1 = pygame.Surface([self.gapStart*self.screen_size[0], config.WALL_HEIGHT]) # Creating the surface for the first part
        gap = pygame.Surface([config.WALL_GAP/100*self.screen_size[0], config.WALL_HEIGHT]) # Creating the surface for the gap
        part2 = pygame.Surface([self.screen_size[0] - part1.get_width() - gap.get_width(), config.WALL_HEIGHT]) # Creating the surface for the second part

        # Fill both parts with RED
        part1.fill('red')
        part2.fill('red')

        self.image = pygame.Surface([self.screen_size[0], config.WALL_HEIGHT]) # Creating the combined surface
        self.image.blit(part1, (0, 0)) # Adding the first part to the combined surface
        self.image.blit(gap, (part1.get_width(), 0)) # Adding the gap to the combined surface
        self.image.blit(part2, (part1.get_width() + gap.get_width(), 0)) # Adding the second part to the combined surface

        self.image.set_colorkey('black') # Removes the black from the gap

        self.rect = self.image.get_rect() # Creating the wall rect
        self.rect.x = 0 # Setting the x position for the rect
        self.rect.y = self.y # Setting the y position for the rect

    # Check if it is time for a new wall
    def newWall(self):
        # If the wall reaches the wall distance: turn self.hasChild to True and return True so that the new wall can be created
        if (not self.hasChild and self.rect.y <= self.screen_size[1] - (config.WALL_DISTANCE + config.WALL_HEIGHT)):
            self.hasChild = True
            return True

    # Update to the newly changed speed
    def updateSpeed(self, speed):
        """changing the wall speed
        updateSpeed(speed): return None
        """
        self.speed = speed

    def update(self):
        self.rect.y -=self.speed

        # Kill wall when it reaches the top
        if (self.rect.y <= -config.WALL_HEIGHT):
            self.kill()