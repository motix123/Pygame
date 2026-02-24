# Example file showing a circle moving on screen
import pygame

# pygame setup
width_screen=1700
height_screen=900
pygame.init()
class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, type, width, height,player_posx,player_posy):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.width=width
        self.height=height
        self.speed=1000
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        if type==1:
           self.image = pygame.image.load("l.png")
        elif type==2:
           self.image = pygame.image.load("zakl.png")
        else:
           self.image = pygame.image.load("lod.png")
        self.image = pygame.transform.scale(self.image,(50,50))


        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.x=player_posx
        self.rect.y=player_posy

    def move_left(self):
        self.x -= self.speed*dt

    def move_right(self):
        self.x += self.speed*dt

    @property
    def x(self):
        return self.rect.x
    @x.setter
    def x(self, value):
        self.rect.x = min(max(0,value), width_screen - self.width)

    def move_up(self):
        self.y -= self.speed*dt

    def move_down(self):
        self.y += self.speed*dt

    @property
    def y(self):
        return self.rect.y
    @y.setter
    def y(self, value):
        self.rect.y = min(max(0,value), height_screen - self.height)

player1 = Player(1, 50, 50,0, 0)
player2 = Player(2, 51, 50,1500, 850)

all_players = pygame.sprite.Group()

all_players.add([player1])
all_players.add([player2])

screen = pygame.display.set_mode((width_screen, height_screen))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    all_players.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player2.move_up()
    if keys[pygame.K_DOWN]:
        player2.move_down()
    if keys[pygame.K_LEFT]:
        player2.move_left()
    if keys[pygame.K_RIGHT]:
        player2.move_right()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move_up()
    if keys[pygame.K_s]:
        player1.move_down()
    if keys[pygame.K_a]:
        player1.move_left()
    if keys[pygame.K_d]:
        player1.move_right()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for frame rate-
    # independent physics.
    dt = clock.tick(20) / 1000

pygame.quit()

# Example file showing a circle moving on screen
"""import pygame

# pygame setup
pygame.init()


class Hrac(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("lod.png")

        self.rect = self.image.get_rect()


hrac1 = Hrac("red", 200, 50)

vsichni_hraci = pygame.sprite.Group()
vsichni_hraci.add(hrac1)

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Hlavní smyčka
while running:

    ## Zpracování vstupu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    ## Výpočty ve hře

    ## Zobrazení stavu na monitor
    screen.fill("purple")  # smazat starý stav

    # vykreslit nový stav
    pygame.draw.circle(screen, "red", player_pos, 40)
    vsichni_hraci.draw(screen)

    pygame.display.flip()  # odeslání změn na monitor

    ## Pauza pro FPS
    dt = clock.tick(60) / 1000  # pauza + kolik času uběhlo v sekundách

pygame.quit()"""
