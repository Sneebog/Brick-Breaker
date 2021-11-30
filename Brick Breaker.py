import pygame
import random
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
FUNNY = (69, 42, 69)
CHIMBUS = (80, 160, 80)
PLIMBEY = (145, 141, 12)
BACKGROUND = (23, 255, 247)
PINKY = (230, 41, 173)
BORDER = (63, 65, 69)
YELLOW = (235, 229, 52)
GREEN = (52, 235, 52)
colour = RED
player_color = RED
answer = 420
# make the functions for the different screens
def startscreen():
    class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    class Block(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            # Call the parent class (Sprite) constructor
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.rect = self.image.get_rect()   
        def update(self):
            mouse_pos = pygame.mouse.get_pos()
            mouse_buttons = pygame.mouse.get_pressed()
            if (mouse_pos[0] > startblock.rect.x and mouse_pos[0] < startblock.rect.x + 70) and (mouse_pos[1] > startblock.rect.y and mouse_pos[1] < startblock.rect.y + 50) :
                if mouse_buttons[0] == True: 
                        answer = game()
                        return answer
            if (mouse_pos[0] > quitblock.rect.x and mouse_pos[0] < quitblock.rect.x + 70) and (mouse_pos[1] > quitblock.rect.y and mouse_pos[1] < quitblock.rect.y + 50) :
                if mouse_buttons[0] == True: 
                    return -1

    Background = Background("Startscreen.jpg", [0,80])
    # Initialize Pygame
    pygame.init()
    # Set the height and width of the screen
    screen_width = 500
    screen_height = 650
    screen = pygame.display.set_mode([screen_width, screen_height])
    #create fonts
    outfit = pygame.font.SysFont('Outfit-Bold.ttf', 50)
    outfitsmall = pygame.font.SysFont('Outfit-Bold.ttf', 40)
    #name the window and play the background music
    pygame.display.set_caption("Startscreen")
    pygame.mixer.init()
    pygame.mixer.music.load("startscreen music.mp3")
    pygame.mixer.music.play(-1,0.0)
    # Loop until the user clicks the close button.
    done = False
    #create sprite list
    all_sprites_list = pygame.sprite.Group()
    quitblock = Block(BLUE, 70, 50)
    startblock = Block(BLUE, 70, 50)
    all_sprites_list.add(quitblock)
    all_sprites_list.add(startblock)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
        # Clear the screen
        screen.fill(BLACK)
        #set the background image
        screen.blit(Background.image, Background.rect)
        #draw borders
        pygame.draw.rect(screen,BORDER, [0, 0, 10, 700 ])
        pygame.draw.rect(screen,BORDER, [490, 0, 10, 700 ])
        pygame.draw.rect(screen,BORDER, [0, 0, 500, 10 ])
        pygame.draw.rect(screen,BORDER, [0, 640, 500, 10 ])
        pygame.draw.rect(screen,BORDER, [0, 70, 500, 10 ])
        #draw boxes for quit and start
        startblock.rect.x, startblock.rect.y = 75, 390
        quitblock.rect.x, quitblock.rect.y = 350, 390
        # Calls update() method on every sprite in the list
        answer = quitblock.update()
        if answer == 0 or answer == 1 or answer == -1:
            done = True
        # Draw all the sprites
        all_sprites_list.draw(screen)
        #draw text for quit and start 
        quit = outfitsmall.render("Quit", True, RED)
        start = outfitsmall.render("Start", True, RED)
        screen.blit(start, (80, 400))
        screen.blit(quit, (355, 400))
        #draw Startscreen text
        Name = outfit.render("Welcome to Brick Breaker !!",  True, RED)
        screen.blit(Name, (20, 20))
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)
    #display the outcome
    return answer
def game():
    #define some variables
    x_speed = 0
    playerx = 250
    xball, yball = 285, 305
    outcome = -1
    xoffset, yoffset = 3, 3
    numcolor = 0 
    poweruptimer = 0
    #Create Classes
    class Block(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.color = color
            self.rect = self.image.get_rect()
    class Ball(pygame.sprite.Sprite):
        ball_hit_list = []
        def __init__(self, color, width, height, speed ):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.width = width
            self.height = height
            self.image.fill(color)
            self.speed = speed
            self.rect = self.image.get_rect()
        def powerup(self):
            self.image = pygame.Surface([self.width * 2, self.height * 2])
            self.image.fill(BLUE)
        def powerup2(self):
            self.speed = 0.75
            self.image.fill(YELLOW)
        def unpowerup(self):
            self.speed = 1
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(RED)
    class Player(pygame.sprite.Sprite):
        def __init__(self, color, width, height,):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.width = width
            self.height = height
            self.image.fill(color)
            self.rect = self.image.get_rect()
        def powerup(self):
            self.image = pygame.Surface([self.width * 1.5, self.height])
            self.image.fill(GREEN)
        def unpowerup(self):
            self.image = pygame.Surface([self.width, self.height])
            self.image.fill(RED)
    class Powerup(pygame.sprite.Sprite):
        def __init__(self, color, width, height):
            super().__init__()
            self.image = pygame.Surface([width, height])
            self.image.fill(color)
            self.color = color
            self.rect = self.image.get_rect()
        def update(self):
            self.rect.y += 2
    class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    Background = Background("stimbo.jpg", [0,80])
    # Initialize Pygame
    pygame.init()
    # Set the height and width of the screen
    screen_width = 500
    screen_height = 650
    screen = pygame.display.set_mode([screen_width, screen_height])
    #create fonts
    outfit = pygame.font.SysFont('Outfit-Bold.ttf', 35)
    #name the window and play the background music
    pygame.display.set_caption("Brick Breaker")
    #Make the sprite lists
    block_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    powerup_list = pygame.sprite.Group()
    #create the blocks
    for i in range(4, 10):
        powerupcolour = random.randint(1,15)
        if i == 4:
            colour = RED
        elif i == 5:
            colour =  BLUE
        elif i == 6:
            colour = BLACK
        elif i == 7:
            colour = FUNNY
        elif i == 8:
            colour = CHIMBUS
        elif i == 9:
            colour = PINKY
        for j in range(12):
            colourblock = colour
            if j == powerupcolour:
                colourblock = PLIMBEY
            # This represents a block
            block = Block(colourblock, 38, 15)
            # Set a location for the block
            block.rect.x = ((j * 40) + 10)
            block.rect.y = (i * 20)
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)
    # Create a player block
    player = Player(RED, 70, 10)
    player.speed = 1
    all_sprites_list.add(player)
    #create a ball
    ball = Ball(RED, 6, 5, 1)
    all_sprites_list.add(ball)
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    score = 0
    while not done:
        #set Win conditions
        if len(block_list) == 0:
            done = True
            outcome = 1
        elif yball > 625:
            done = True
            outcome = 0
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN:
                # Figure out if it was an arrow key. If so
                # adjust speed
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_speed = 0
            if event.type == pygame.QUIT:
                done = True
        # Clear the screen
        screen.fill(BACKGROUND)
        #set the background image
        screen.blit(Background.image, Background.rect)
        #draw borders
        pygame.draw.rect(screen,BORDER, [0, 0, 10, 700 ])
        pygame.draw.rect(screen,BORDER, [490, 0, 10, 700 ])
        pygame.draw.rect(screen,BORDER, [0, 0, 500, 10 ])
        pygame.draw.rect(screen,BORDER, [0, 640, 500, 10 ])
        pygame.draw.rect(screen,BORDER, [0, 70, 500, 10 ])
        #draw the scoreboards and the title
        score_board = outfit.render("SCORE: " +  str(score),  True, BLUE)
        highscore_board = outfit.render("HIGHSCORE: " + str(6 * 12 * 20),  True, BLUE)
        screen.blit(score_board, (250, 20))
        screen.blit(highscore_board, (250, 40))
        title1 = outfit.render("BRICK", True, RED)
        title2 = outfit.render("BREAKER", True, RED)
        screen.blit(title1, (60, 20))
        screen.blit(title2, (50, 40))
        #stop the paddles going off the screen
        if  (player.rect.x) - 5 <= 0:
            playerx += 5
            x_speed = 0
        elif player.rect.x + 5>= 430:
            playerx -= 5 
            x_speed = 0
        #Make the paddle and the ball move
        playerx += x_speed 
        player.rect.x = playerx
        player.rect.y = 600
        xball -= xoffset * ball.speed
        yball -= yoffset * ball.speed
        ball.rect.x = xball 
        ball.rect.y = yball 
        #make the ball bounce off the screen
        if xball < 10 or xball >= 480:
            xoffset = xoffset * -1
        if yball < 80 or yball >= 630:
            yoffset = yoffset * -1
        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(ball, block_list, True)
        powerup_hit_list = pygame.sprite.spritecollide(player, powerup_list, True)
        #Make ball bounce of padde(change this to spritecollide)
        if pygame.sprite.collide_rect(ball, player) == True:
            if x_speed == -5:
                xoffset = xoffset * -1
            yoffset = yoffset * -1 
            yball -= yoffset + random.randint(1, 3)
        # Check the list of collisions.
        #Make Powerups
        if len(blocks_hit_list) > 0:
            yoffset = yoffset * -1 
            if random.randint(1,2) == 2:
                numcolor = random.randint(1,3)
                if numcolor == 1:
                    powerupcolour = BLUE
                elif numcolor == 2:
                    powerupcolour = YELLOW
                else:
                    powerupcolour = RED
                power = Powerup(powerupcolour, 20, 10 )
                all_sprites_list.add(power)
                powerup_list.add(power)
                power.rect.x = ball.rect.x
                power.rect.y = ball.rect.y 
        #make different colours for each power up  
        if len(powerup_hit_list) > 0:
            if powerup_hit_list[0].color == BLUE:
                    ball.powerup()
                    poweruptimer = 300
            elif powerup_hit_list[0].color == RED:
                    player.powerup()
                    poweruptimer = 300
            else:
                    ball.powerup2()
                    poweruptimer = 300
        #make powerup duration
        if poweruptimer == 0:
            ball.unpowerup()
            player.unpowerup()
        else:
            poweruptimer -= 1
        #add a scoreboardblock in blocks_hit_list:
        for block in blocks_hit_list:
            score += 20
        # Draw all the spites
        powerup_list.update()
        all_sprites_list.draw(screen)
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)
    #display the outcome for the gameover screen
    return outcome
def gameoverscreen(music, image,text, windowname ):
    class Background(pygame.sprite.Sprite):
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    #make a timer for the gameover screen
    gameover_timer = 0
    gameover = False 
    # Initialize Pygame
    pygame.init()
    #create a font
    outfitreg = pygame.font.SysFont('Outfit-Regular.ttf', 75)
    clock = pygame.time.Clock()
    #name the window and play the background music
    pygame.display.set_caption(windowname)
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1,0.0)
    # Set the height and width of the screen
    Background = Background(image, [0,0])
    # Set the height and width of the screen
    screen_width = 500
    screen_height = 650
    screen = pygame.display.set_mode([screen_width, screen_height])
    #create the screen
    while not gameover:
        if gameover_timer == 600:
            gameover = True
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                gameover = True
        # Clear the screen
        screen.fill(BLACK)
        #set the background image
        screen.blit(Background.image, Background.rect)
        Gameoverscreen = outfitreg.render(text, True, RED)
        screen.blit(Gameoverscreen, (125, 250))
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)
        #set the timer
        gameover_timer += 1
        pygame.quit
#run the program
answer = startscreen()
if answer == 1:
    gameoverscreen("Win music.mp3", "Win screen.jpg", "Congratulations", "Victory Screen 3")
elif answer == 0:
    gameoverscreen("Lose music.mp3", "Lose screen.jpg", "You are awful", "Lose Screen 7")