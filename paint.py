import pygame

pygame.init()

W, H = 800, 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Paint")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(WHITE)
clock = pygame.time.Clock()

drawing = False
color = BLACK
size = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_e:
                color = WHITE
            elif event.key == pygame.K_UP:
                size += 2
            elif event.key == pygame.K_DOWN:
                size = max(1, size - 2)
    
    if drawing:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), size)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
