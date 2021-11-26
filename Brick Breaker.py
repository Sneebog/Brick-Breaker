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
colour = RED
player_color = RED
#define some variables
x_speed = 0
playerx = 250
xball, yball = 285, 305
answer = "" 
speedtimer = 0
xoffset, yoffset = 3, 3
nonraxoffset, nonrayoffset = 3, 3

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
        self.image.fill(color)
        self.speed = speed
        self.rect = self.image.get_rect()
    def powerup(self):
        if self.powerup > 0:
            self.powerup -= 1
class player(pygame.sprite.Sprite):
    def __init__(self, color, width, height,):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    def abilities(self, speed):
        self.speed = speed
    def powerup(self,num):
        if num > 0:
            num -= 1 
            return 2   
        else:
            return 1
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
#Create Functions
def write(text, color, size, fontPath):
        font = pygame.font.Font(fontPath, size)
        text = font.render(text, 1, pygame.Color(color))
        return 
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
pygame.display.set_caption("Project Plimble")
#Make the sprite lists
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
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
player = player(RED, 70, 10)
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
        answer = "congratulation"
    elif yball > 625:
        done = True
        answer = "you are awful"
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
    highscore_board = outfit.render("HIGHSCORE: " + str(7 * 12 * 20),  True, BLUE)
    screen.blit(score_board, (250, 20))
    screen.blit(highscore_board, (250, 40))
    title1 = outfit.render("STUNNA", True, RED)
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
    playerx += (x_speed * player.speed)
    player.rect.x = playerx
    player.rect.y = 600
    xball -= xoffset 
    yball -= yoffset 
    ball.rect.x = xball
    ball.rect.y = yball
    #make the ball bounce off the screen
    if xball < 10 or xball >= 480:
        xoffset = xoffset * -1
    if yball < 80 or yball >= 630:
        yoffset = yoffset * -1
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(ball, block_list, True)
    #Make ball bounce of padde(change this to spritecollide)
    if ((ball.rect.y > (player.rect.y - 15)) and (ball.rect.y < (player.rect.y + 50))) and ((ball.rect.x > player.rect.x - 15) and (ball.rect.x < player.rect.x + 50)):
        if x_speed == -5:
             xoffset = xoffset * -1
        yoffset = yoffset * -1 
        yball -= yoffset + random.randint(1, 3)
    # Check the list of collisions.
    #Make Powerups
    if len(blocks_hit_list) > 0:
        yoffset = yoffset * -1 
        if blocks_hit_list[0].color == PLIMBEY:
            player.abilities(player.powerup(200))
            speedtimer = 200
    else:
        speedtimer -= 1
    if speedtimer == 0:
        player.abilities(1)
    #change colour for powerup
    if speedtimer > 0:
        player.color = BLUE
    #add a scoreboardblock in blocks_hit_list:
    for block in blocks_hit_list:
        score += 20
    # Draw all the spites
    all_sprites_list.draw(screen)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Limit to 60 frames per second
    clock.tick(60)
#display the outcome
pygame.quit()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
gameover_timer = 0
if answer == "you are awful":
    gameover = False 
    # Initialize Pygame
    pygame.init()
    outfitreg = pygame.font.SysFont('Outfit-Regular.ttf', 75)
    clock = pygame.time.Clock()
    #name the window and play the background music
    pygame.display.set_caption("Game over screen 1")
    pygame.mixer.init()
    pygame.mixer.music.load("Lose music.mp3")
    pygame.mixer.music.play(-1,0.0)
    # Set the height and width of the screen
    Background = Background("Lose screen.jpg", [0,0])
    # Set the height and width of the screen
    screen_width = 500
    screen_height = 650
    screen = pygame.display.set_mode([screen_width, screen_height])
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
        Gameoverscreen = outfitreg.render("GAME OVER", True, RED)
        screen.blit(Gameoverscreen, (125, 250))
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)
        gameover_timer += 1
    pygame.quit
elif answer == "congratulation":
    gameover = False 
    # Initialize Pygame
    pygame.init()
    outfitreg = pygame.font.SysFont('Outfit-Regular.ttf', 75)
    clock = pygame.time.Clock()
    #name the window and play the background music
    pygame.display.set_caption("Game over screen 24")
    pygame.mixer.init()
    pygame.mixer.music.load("congratulations.mp3")
    pygame.mixer.music.play(-1,0.0)
    # Set the height and width of the screen
    Background = Background("Win screen.jpg", [0,0])
    screen_width = 500
    screen_height = 550
    screen = pygame.display.set_mode([screen_width, screen_height])
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
        Gameoverscreen = outfitreg.render("Congatulations", True, RED)
        screen.blit(Gameoverscreen, (100, 250))
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        # Limit to 60 frames per second
        clock.tick(60)
        gameover_timer += 1
    pygame.quit
print(answer)
