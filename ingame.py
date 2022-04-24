import pygame, config
from inGame.player import Player
from inGame.wall import Wall

class Ingame:
    """The Ingame class"""

    def __init__(self) -> None:
        self.createGroups() # Initialize the groups

        self.screen = pygame.display.get_surface() # Fetching the surface

        self.player = Player(self) # Initializing the player
        Wall(self) # Initialize the first wall
        self.wall_speed = 1
        self.i = 0 # Counter used to delay the speed increase

    def createGroups(self):
        """Creating the groups"""
        self.all_sprites = pygame.sprite.LayeredUpdates() # A group containing all sprites
        self.walls = pygame.sprite.LayeredUpdates() # A group for all the walls
        self.coins = pygame.sprite.LayeredUpdates() # A group for all the coins
        self.playerG = pygame.sprite.GroupSingle() # A group for the player

    def changeWallSpeed(self):
        if (self.i == 10*60):
            print("WallSpeed: +1")
            self.wall_speed += 1
            self.i = 0 
        self.i += 1

    def update(self):
        self.changeWallSpeed() # Adjust the wall speed

        self.all_sprites.update() # Update all the sprites

        for wall in self.walls:
            # Update the wall speed if changed
            if (not (wall.speed == self.wall_speed)):
                wall.updateSpeed(self.wall_speed)

            # Check if it is time for a new wall
            if (wall.newWall()):
                Wall(self)

        if (not (wall.speed == self.wall_speed)):
            self.player.updateSpeed(self.wall_speed) # Telling the player about the changed speed
        
        
        self.all_sprites.draw(self.screen) # Draw all the sprites
        #return 'menu'