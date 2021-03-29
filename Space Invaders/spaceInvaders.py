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

def player():
    screen.blit(playerImg, (playerX, playerY))

# Loop para asegurarse que la ventana se quede prendida hasta que cerremos el juego
# Event es algo que sucede en el juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Definimos que van a hacer las teclas en el juego
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.KEY_LEFT:
            print("Left arrow is pressed.")
        if event.key == pygame.KEY_RIGHT:
            print("Right arrow is pressed.")
    if event.type == pygame.KEYUP:
        if event.key == pygame. KEY_LEFT or pygame.K_RIGHT:
            print("Keystoke has been released.")


    screen.fill((0, 0, 0)) # RGB color para el fondo
    # Poner el player despues de la screen porque sino estaria dibujado abajo de la pantalla y no arriba
    player()
    pygame.display.update() # Actualizamos para aplicar lo que pasa en el loop a la pantalla
