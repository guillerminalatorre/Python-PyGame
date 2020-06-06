import pygame
 
pygame.init()

pantalla = pygame.display.set_mode((640, 480))
reloj = pygame.time.Clock()
hecho = False
 

font = pygame.font.SysFont("quando", 85)
pygame.display.set_caption("Harry Potter Quidditch")
text = font.render("Hola, Mundo", True, (0, 139, 139))
 
while not hecho:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            hecho = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            hecho = True
 
    pantalla.fill((255, 255, 255))
    pantalla.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    reloj.tick(60)
    
    
   