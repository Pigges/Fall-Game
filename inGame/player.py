import pygame, config

class Player(pygame.sprite.Sprite):
    """The Player class
    \nNeeds 'game' (the parent class)"""

    def __init__(self, game: object) -> None:
        self.game = game # Assign the game(parent class) to self.game for later use
        self._layer = config.PLAYER_LAYER
        self.groups = self.game.playerG, self.game.all_sprites # Assigns the groups
        pygame.sprite.Sprite.__init__(self, self.groups) # Initialize the sprite
        self.screen_size = pygame.display.get_window_size() # Fetching the screen size [list] usage: x: [0], y: [1]

        self.image = pygame.Surface([config.PLAYER_SIZE, config.PLAYER_SIZE]) # Create a surface
        self.image.set_colorkey('black') # Removes the black from the surface
        pygame.draw.circle(self.image, 'blue', (config.PLAYER_SIZE/2, config.PLAYER_SIZE/2), config.PLAYER_SIZE/2) # Draw a circle on the surface

        self.rect = self.image.get_rect() # Get the rect of the surface
        self.rect.x = 100 # Set the x value of the rect
        self.rect.y = 100 # Set the y value of the rect

        self.vel = pygame.Vector2(0, 0)
        self.falling = True

        self.speed = 1

    def applyVelocity(self):
        self.vel.y = self.speed # Add fall velocity

        self.falling = True
        # Applying the movement in x
        self.rect.x += self.vel.x

        # If x collides with the screen edge
        if (self.rect.x <= 0):
            self.rect.x = 0
        elif (self.rect.x >= self.screen_size[0] - config.PLAYER_SIZE):
            self.rect. x = self.screen_size[0] - config.PLAYER_SIZE
        

        # Applying the movement in y
        self.rect.y += self.vel.y

        # If collision in y move back to previous position
        while (pygame.sprite.spritecollide(self, self.game.walls, False)):
            self.rect.y -= 1
            #self.falling = False

        self.vel.x = 0
        self.vel.y = 0

    def checkMovement(self):
        keys = pygame.key.get_pressed()

        # Checking keys and run the appropriate code.
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel.x = -config.PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel.x = config.PLAYER_SPEED

    # Update to the newly changed speed
    def updateSpeed(self, speed):
        """changing the wall speed
        updateSpeed(speed): return None
        """
        self.speed = speed


    def update(self):

        self.checkMovement() # Checking and then applying the movement
        
        self.applyVelocity() # Applying the velocity