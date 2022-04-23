import pygame, config
from inGame.player import Player
from inGame.wall import Wall

class Ingame:
    """The Ingame class"""

    def __init__(self) -> None:
        self.createGroups() # Initialize the groups

        self.player = Player() # Initializing the player
        self.walls = [Wall(self)] # Initialize the first wall in a list

    def createGroups(self):
        """Creating the groups"""
        self.all_sprites = pygame.sprite.LayeredUpdates() # A group containing all sprites
        self.walls = pygame.sprite.LayeredUpdates # A group for all the walls
        self.coins = pygame.sprite.LayeredUpdates() # A group for all the coins
        self.playerG = pygame.sprite.GroupSingle() # A group for the player

    def update(self):
        pass
        #return 'menu'