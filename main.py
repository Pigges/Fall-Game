import pygame, math, sys, menu, ingame, gameover, config


"""'state': [state.Class, Object || None]"""
gameStates={
    'menu': [menu.Menu, None],
    'ingame': [ingame.Ingame, None],
    'gameover': [gameover.Gameover, None]
}


class Game():
    """The main class for this game"""

    def __init__(self) -> None:
        pygame.init() # Initializing pygame
        self.screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT),pygame.RESIZABLE) # Creating the display window
        pygame.display.set_caption(config.TITLE) # Setting the title of the window
        # pygame_icon = pygame.image.load(config.ICON).convert() # Loading the window icon
        # pygame.display.set_icon(pygame_icon) # Setting the window icon
        self.clock = pygame.time.Clock() # Creating a clock for the game
        self.font = pygame.font.SysFont('arial', 32) # Setting the game font
        
        self.state = None # Initiate the state
        self.handleStateChange('ingame') # Set the state

        """Game states: see gameStates"""

    def clearScreen(self):
        self.screen.fill('black')

    def events(self):
        """Handling events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user wants to quit then do so accordingly
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                pass

    def handleStateChange(self, newState: str):
        """Handle state changes"""
        if newState in gameStates: # Verify that the requested state is a valid one
            self.state = newState # Change to the newState
            gameStates[self.state][1] = gameStates[self.state][0]() # Initialize new state
            print(f"newState: {self.state}")
        else: return False # If not valid: return False
        return True # Otherwise, if valid: return True

    def handleGameState(self):
        response = gameStates.get(self.state)[1].update() # Update the current state
        if (response): # Should return something if should change gameState
            self.handleStateChange(response) # If response: change gameState

    def main(self):
        '''The main function'''

        while True:
            self.clearScreen() # Clear the screen before continuing
            self.events()

            self.handleGameState() # Run the appropriate state         

            self.clock.tick(config.FPS) # Set tick delay
            pygame.display.flip() # Update the display to show the new content


game = Game()
game.main()