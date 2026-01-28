import pygame
import random

# Inicializar pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (213, 50, 80)
VERDE = (0, 255, 0)

# Tamaño de la ventana
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake")

# Reloj
reloj = pygame.time.Clock()
velocidad = 15

# Tamaño de bloque
tam_bloque = 10

# Fuente
fuente = pygame.font.SysFont("arial", 25)


def mostrar_puntaje(puntaje):
    texto = fuente.render(f"Puntaje: {puntaje}", True, BLANCO)
    pantalla.blit(texto, [0, 0])


def dibujar_serpiente(tam_bloque, lista_serpiente):
    for x in lista_serpiente:
        pygame.draw.rect(pantalla, VERDE, [x[0], x[1], tam_bloque, tam_bloque])


def mensaje(texto, color):
    msg = fuente.render(texto, True, color)
    pantalla.blit(msg, [ANCHO / 6, ALTO / 3])


def juego():
    game_over = False
    game_close = False

    x = ANCHO / 2
    y = ALTO / 2
    dx = 0
    dy = 0

    serpiente = []
    longitud = 1

    comida_x = round(random.randrange(0, ANCHO - tam_bloque) / 10) * 10
    comida_y = round(random.randrange(0, ALTO - tam_bloque) / 10) * 10

    while not game_over:

        while game_close:
            pantalla.fill(NEGRO)
            mensaje("Perdiste! Presiona C para continuar o Q para salir", ROJO)
            mostrar_puntaje(longitud - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        juego()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    dx = -tam_bloque
                    dy = 0
                elif evento.key == pygame.K_RIGHT:
                    dx = tam_bloque
                    dy = 0
                elif evento.key == pygame.K_UP:
                    dy = -tam_bloque
                    dx = 0
                elif evento.key == pygame.K_DOWN:
                    dy = tam_bloque
                    dx = 0

        if x >= ANCHO or x < 0 or y >= ALTO or y < 0:
            game_close = True

        x += dx
        y += dy
        pantalla.fill(NEGRO)
        pygame.draw.rect(pantalla, ROJO, [comida_x, comida_y, tam_bloque, tam_bloque])
        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        serpiente.append(cabeza)
        if len(serpiente) > longitud:
            del serpiente[0]

        for bloque in serpiente[:-1]:
            if bloque == cabeza:
                game_close = True

        dibujar_serpiente(tam_bloque, serpiente)
        mostrar_puntaje(longitud - 1)

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ANCHO - tam_bloque) / 10) * 10
            comida_y = round(random.randrange(0, ALTO - tam_bloque) / 10) * 10
            longitud += 1

        reloj.tick(velocidad)

    pygame.quit()
    quit()


juego()
