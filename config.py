import pygame

#loading images
pikachu = pygame.image.load('Player1.png')
syduckwin = pygame.image.load('Player2_won.png')
syduk = pygame.image.load('Player2.png')
pikachuwin = pygame.image.load('Player1_won.png')
crown = pygame.image.load('Crown.png')

#initialising game window
game = pygame.display.set_mode((1800, 1000))
pygame.init()
pygame.display.set_caption('Pika VS Syduck')
clock = pygame.time.Clock()

#Different variable
level1 = 0
level2 = 0
poke = 1
Score1 = 0
Score2 = 0
count = 0
vel1 = 2
vel2 = 2
vel = 10
s1 = []
s2 = []
p1 = 1
minute1 = 0
minute2 = 0
second1 = 0
second2 = 0
frame_count1 = 0
frame_count2 = 0
frame_rate = 60

# player pikachu
class player1(object):

    def __init__(
        self,
        x,
        y,
        width,
        height,
        ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x, self.y, 50, 50)

    def make(self, game):
        game.blit(pikachu, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 50)


# player syduck
class player2(object):

    def __init__(
        self,
        x,
        y,
        width,
        height,
        ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.hitbox = (self.x, self.y, 50, 50)

    def make(self, game):
        game.blit(syduk, (self.x, self.y))
        self.hitbox = (self.x, self.y, 50, 50)

# moving obstacle
class enemy2(object):

    enemy2 = pygame.image.load('Static_enemy.png')

    def __init__(
        self,
        x,
        y,
        width,
        height,
        ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, 70, 70)

    def draw(self, game):
        game.blit(self.enemy2, (self.x, self.y))
        self.hitbox = (self.x, self.y, 70, 70)


# standing obstacle....
class enemy1(object):

    global poke
    global level1
    global level2
    enemy1 = pygame.image.load('Moving_enemy.png')

    def __init__(
        self,
        x,
        y,
        width,
        height,
        end,
        ):
        global level1
        global level2
        global player
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.hitbox = (self.x, self.y, 70, 70)

    def draw(self, game, vel):
        self.move(vel)
        game.blit(self.enemy1, (self.x, self.y))
        self.hitbox = (self.x, self.y, 70, 70)

    def move(self, vel):
        if self.x < self.path[1] + vel:
            self.x = vel + self.x
        else:
            self.x = self.path[0]


#font types
font1 = pygame.font.SysFont('comicsans', 100, True)
font = pygame.font.SysFont('comicsans', 30, True)
text9 = font.render('ohno! better you have pressed key x', 1, (0, 0, 0))
text10 = font1.render('restart the game', 1,(0,0,0))
text11 = font1.render('better luck next time', 1,(0,0,0))

#Onscreen drawing diff characters
pika = player1(800, 950, 50, 50)
syduck = player2(800, 0, 50, 50)
crab = enemy1(1000, 100, 70, 70, 1800)
crab5 = enemy1(0, 100, 70, 70, 1000)
crab1 = enemy1(0, 280, 70, 70, 1000)
crab2 = enemy1(110, 460, 70, 70, 1000)
crab6 = enemy1(1100, 460, 70, 70, 1800)
crab3 = enemy1(0, 640, 70, 70, 1500)
crab4 = enemy1(500, 820, 70, 70, 1800)
plant = enemy2(300, 870, 70, 70)
plant1 = enemy2(900, 720, 70, 70)
plant2 = enemy2(700, 540, 70, 70)
plant3 = enemy2(1650, 360, 70, 70)
plant4 = enemy2(550, 190, 70, 70)
plant5 = enemy2(1700, 870, 70, 70)
plant6 = enemy2(300, 540, 70, 70)
plant7 = enemy2(400, 360, 70, 70)
plant8 = enemy2(200, 20, 70, 70)
plant9 = enemy2(100, 720, 70, 70)
plant10 = enemy2(1400, 20, 70, 70)
plant11 = enemy2(1000, 190, 70, 70)
plant12 = enemy2(1000, 360, 70, 70)
plant13 = enemy2(1500, 540, 70, 70)