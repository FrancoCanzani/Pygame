import pygame

# Iniciar pygame
pygame.init()

# Crear la pantalla con el alto y ancho en pixeles
screen = pygame.display.set_mode((800, 600))

# Titulo e icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("cohete.png")
pygame.display.set_icon(icon)

# Nave espacial del juego
playerImg = pygame.image.load("Nave espacial.png")
playerX = 370 # Donde va a estar situado
playerY = 480
playerX_Change = 0

# Enemigo
playerImg = pygame.image.load("alien.png")
playerX = 370 # Donde va a estar situado
playerY = 480
playerX_Change = 0

def player():
    screen.blit(playerImg, (playerX, playerY))

# Loop para asegurarse que la ventana se quede prendida hasta que cerremos el juego
# Event es algo que sucede en el juego
running = True
while running:

    screen.fill((0, 0, 0)) # RGB color para el fondo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Definimos que van a hacer las teclas en el juego
        if event.type == pygame.KEYDOWN:
            print("A keystoke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_Change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_Change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_Change = 0

    playerX += playerX_Change # Hace que se vaya modificando la posicion de la nave a medida que tocamos las felchas.

# Delimitamos los limites de la nave para que no se pase afuera de la pantalla
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Poner el player despues de la screen porque sino estaria dibujado abajo de la pantalla y no arriba
    player()
    pygame.display.update() # Actualizamos para aplicar lo que pasa en el loop a la pantalla
