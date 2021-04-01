import pygame
import random
import math

# Iniciar pygame
pygame.init()

# Crear la pantalla con el alto y ancho en pixeles
screen = pygame.display.set_mode((800, 600))

# Fondo
background = pygame.image.load("fondo.png")

# Titulo e icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("cohete.png")
pygame.display.set_icon(icon)

# Nave espacial del juego
playerImg = pygame.image.load("Nave espacial.png")
playerX = 370  # Donde va a estar situado
playerY = 480
playerX_Change = 0

# Enemigo
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0, 735)  # Donde va a estar situado
enemyY = random.randint(50, 150)
enemyX_Change = 0.2
enemyY_Change = 40

# Bala
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_Change = 0
bulletY_Change = 2
bullet_state = "Ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 20, y + 10))


# Usamos la formula de la distancia entre dos coordenadas para la colision (d=√((x_2-x_1)²+(y_2-y_1)²))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


# Loop para asegurarse que la ventana se quede prendida hasta que cerremos el juego
# Event es algo que sucede en el juego
running = True
while running:

    # RGB color para el fondo
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Definimos que van a hacer las teclas en el juego
        if event.type == pygame.KEYDOWN:
            #print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "Ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change  # Hace que se vaya modificando la posicion de la nave a medida que tocamos las felchas.

    # Delimitamos los limites de la nave y el enemigo para que no se pase afuera de la pantalla
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_Change

    if enemyX <= 0:
        enemyX_Change = 0.2
        enemyY += enemyY_Change
    elif enemyX >= 736:
        enemyX_Change = -0.2
        enemyY += enemyY_Change

    # Movimiento de la bala
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "Ready"
    if bullet_state == "Fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_Change

    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "Ready"
        score += 1
        print(f"Puntos: {score}")
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    # Poner el player despues de la screen porque sino estaria dibujado abajo de la pantalla y no arriba
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  # Actualizamos para aplicar lo que pasa en el loop a la pantalla
