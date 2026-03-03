"""# Example file showing a circle moving on screen
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

all_players = pygame.sprite.Group()

all_players.add([player1])

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
    screen.fill("#100010")
    all_players.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.move_up()
    if keys[pygame.K_DOWN]:
        player1.move_down()
    if keys[pygame.K_LEFT]:
        player1.move_left()
    if keys[pygame.K_RIGHT]:
        player1.move_right()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for frame rate-
    # independent physics.
    dt = clock.tick(90) / 1000

pygame.quit()"""

import pygame
import random
import sys

# Inicializace
pygame.init()

# Okno
WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Barvy
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Hodiny
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.SysFont("arial", 32)

# Pták
bird_x = 80
bird_y = HEIGHT // 2
bird_radius = 20
bird_velocity = 0
gravity = 0.5
jump_strength = -8

# Trubky
pipe_width = 70
pipe_gap = 180
pipe_velocity = 3
pipes = []

# Skóre
score = 0

# Čas
start_time = 0


def create_pipe():
    height = random.randint(150, 400)
    top_pipe = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_pipe = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top_pipe, bottom_pipe


def reset_game():
    global bird_y, bird_velocity, pipes, score, start_time
    bird_y = HEIGHT // 2
    bird_velocity = 0
    pipes = []
    score = 0
    start_time = pygame.time.get_ticks()


def draw_window(elapsed_time):
    WIN.fill(BLUE)

    # Pták
    pygame.draw.circle(WIN, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Trubky
    for top_pipe, bottom_pipe in pipes:
        pygame.draw.rect(WIN, GREEN, top_pipe)
        pygame.draw.rect(WIN, GREEN, bottom_pipe)

    # Skóre
    score_text = font.render(f"Score: {score}", True, BLACK)
    WIN.blit(score_text, (10, 10))

    # Čas
    time_text = font.render(f"Time: {elapsed_time:.1f}s", True, BLACK)
    WIN.blit(time_text, (10, 50))

    pygame.display.update()


def main():
    global bird_y, bird_velocity, pipes, score

    reset_game()

    running = True
    while running:
        clock.tick(FPS)

        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength

        # Pohyb ptáka
        bird_velocity += gravity
        bird_y += bird_velocity

        # Přidání trubek
        if len(pipes) == 0 or pipes[-1][0].x < WIDTH - 250:
            pipes.append(create_pipe())

        # Pohyb trubek
        for pipe in pipes:
            pipe[0].x -= pipe_velocity
            pipe[1].x -= pipe_velocity

        # Odstranění trubek mimo obraz
        pipes = [pipe for pipe in pipes if pipe[0].x > -pipe_width]

        # Kolize
        bird_rect = pygame.Rect(
            bird_x - bird_radius,
            bird_y - bird_radius,
            bird_radius * 2,
            bird_radius * 2
        )

        for top_pipe, bottom_pipe in pipes:
            if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
                reset_game()

        if bird_y <= 0 or bird_y >= HEIGHT:
            reset_game()

        # Skóre
        for pipe in pipes:
            if pipe[0].x + pipe_width == bird_x:
                score += 1

        draw_window(elapsed_time)


if __name__ == "__main__":
    main()