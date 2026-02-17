# Example file showing a circle moving on screen
import pygame

# pygame setup

pygame.init()
class Player(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, width, height,player_posx,player_posy):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect.x=player_posx
       self.rect.y=player_posy

player1 = Player("#700083", 200, 50,0, 0)
player2 = Player("#00ff55", 200, 50,1500, 900)

all_players = pygame.sprite.Group()

all_players.add(player1)
all_players.add(player2)



screen = pygame.display.set_mode((1700, 900))
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
    pygame.draw.circle(screen,"#700083", player_pos,50)
    all_players.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for frame rate-
    # independent physics.
    dt = clock.tick(60) / 280

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
