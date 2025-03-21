import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Nave vs Meteoritos")

# Colores
WHITE = (255, 255, 255)
RED = (200, 0, 0)

# Jugador
player_size = 50
player = pygame.Rect(WIDTH // 2 - player_size // 2, HEIGHT - 70, player_size, player_size)
player_speed = 7

# Meteoritos
meteor_size = 40
meteors = []
meteor_speed = 5

# Puntuación
score = 0
font = pygame.font.SysFont(None, 40)

def draw_player():
    pygame.draw.rect(screen, WHITE, player)


def draw_meteors():
    for meteor in meteors:
        pygame.draw.rect(screen, RED, meteor)


def draw_score():
    text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def main_menu():
    screen.fill((0, 0, 0))
    title = font.render("Nave vs Meteoritos", True, WHITE)
    instructions = font.render("Presiona ESPACIO para comenzar", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
    screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False


def game_loop():
    global score, meteors, meteor_speed
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

        # Crear meteoritos
        if random.randint(1, 20) == 1:
            meteors.append(pygame.Rect(random.randint(0, WIDTH - meteor_size), 0, meteor_size, meteor_size))

        # Mover meteoritos
        for meteor in meteors[:]:
            meteor.y += meteor_speed
            if meteor.y > HEIGHT:
                meteors.remove(meteor)
                score += 1

            # Colisión
            if player.colliderect(meteor):
                running = False

        # Aumentar dificultad
        if score % 10 == 0 and score > 0:
            meteor_speed += 0.01

        # Dibujar todo
        screen.fill((0, 0, 0))
        draw_player()
        draw_meteors()
        draw_score()

        pygame.display.flip()
        clock.tick(60)

    # Fin del juego
    pygame.time.wait(1000)
    main_menu()


# Iniciar el juego
main_menu()
game_loop()

