import pygame

pygame.init()

pantalla = pygame.display.set_mode((280, 550))
reloj = pygame.time.Clock()
hecho = False
imagen = pygame.image.load("menu.png")

font = pygame.font.SysFont("quando", 50)
pygame.display.set_caption("Harry Potter Quidditch")
text = font.render("Hola, Mundo", True, (0, 139, 139))

def dibujar_botones(lista_botones):
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])


while not hecho:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hecho = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            hecho = True

    pantalla.fill((255, 255, 255))
    pantalla.blit(text, ((280 - text.get_width()) // 2, (550 - text.get_height()) // 3))
    pantalla.blit(imagen, (0, 0))
    pygame.display.update()

    pygame.display.flip()
    reloj.tick(60)


   