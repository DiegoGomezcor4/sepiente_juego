import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de la Serpiente")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Configuración de la serpiente y comida
TAMANIO_CUADRADO = 20
velocidad = 10

# Función para mostrar texto en pantalla
def mostrar_texto(texto, color, posicion, tamaño=40):
    fuente = pygame.font.Font(None, tamaño)
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, posicion)

# Función principal
def juego():
    # Inicialización de la serpiente
    x_snake = ANCHO // 2
    y_snake = ALTO // 2
    cuerpo_snake = [(x_snake, y_snake)]
    direccion = "DERECHA"

    # Inicialización de la comida
    x_comida = random.randint(0, (ANCHO - TAMANIO_CUADRADO) // TAMANIO_CUADRADO) * TAMANIO_CUADRADO
    y_comida = random.randint(0, (ALTO - TAMANIO_CUADRADO) // TAMANIO_CUADRADO) * TAMANIO_CUADRADO

    reloj = pygame.time.Clock()
    en_juego = True

    while en_juego:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Controles de la serpiente
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP and direccion != "ABAJO":
                    direccion = "ARRIBA"
                if evento.key == pygame.K_DOWN and direccion != "ARRIBA":
                    direccion = "ABAJO"
                if evento.key == pygame.K_LEFT and direccion != "DERECHA":
                    direccion = "IZQUIERDA"
                if evento.key == pygame.K_RIGHT and direccion != "IZQUIERDA":
                    direccion = "DERECHA"

        # Movimiento de la serpiente
        if direccion == "ARRIBA":
            y_snake -= TAMANIO_CUADRADO
        if direccion == "ABAJO":
            y_snake += TAMANIO_CUADRADO
        if direccion == "IZQUIERDA":
            x_snake -= TAMANIO_CUADRADO
        if direccion == "DERECHA":
            x_snake += TAMANIO_CUADRADO

        # Actualizar cuerpo de la serpiente
        cuerpo_snake.insert(0, (x_snake, y_snake))
        if x_snake == x_comida and y_snake == y_comida:
            # Generar nueva comida
            x_comida = random.randint(0, (ANCHO - TAMANIO_CUADRADO) // TAMANIO_CUADRADO) * TAMANIO_CUADRADO
            y_comida = random.randint(0, (ALTO - TAMANIO_CUADRADO) // TAMANIO_CUADRADO) * TAMANIO_CUADRADO
        else:
            cuerpo_snake.pop()

        # Fin del juego si la serpiente choca con los bordes o consigo misma
        if (
            x_snake < 0 or x_snake >= ANCHO or
            y_snake < 0 or y_snake >= ALTO or
            len(cuerpo_snake) != len(set(cuerpo_snake))
        ):
            en_juego = False

        # Dibujar en la pantalla
        pantalla.fill(NEGRO)
        for segmento in cuerpo_snake:
            pygame.draw.rect(pantalla, VERDE, (segmento[0], segmento[1], TAMANIO_CUADRADO, TAMANIO_CUADRADO))

        pygame.draw.rect(pantalla, ROJO, (x_comida, y_comida, TAMANIO_CUADRADO, TAMANIO_CUADRADO))

        # Mostrar puntuación
        puntuacion = len(cuerpo_snake) - 1
        mostrar_texto(f"Puntuación: {puntuacion}", BLANCO, (10, 10), 30)

        pygame.display.flip()
        reloj.tick(velocidad)

    # Pantalla de fin del juego
    pantalla.fill(NEGRO)
    mostrar_texto("¡Juego Terminado!", ROJO, (ANCHO // 2 - 100, ALTO // 2 - 50), 50)
    mostrar_texto(f"Puntuación final: {puntuacion}", BLANCO, (ANCHO // 2 - 100, ALTO // 2 + 10), 40)
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == "__main__":
    juego()
