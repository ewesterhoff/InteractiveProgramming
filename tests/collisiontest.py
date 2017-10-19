import pygame

x = y = 0
running = 1
screen = pygame.display.set_mode((600, 400))
pygame.mouse.set_visible(False)

fox_image = pygame.image.load("sword.png")
tree_image = pygame.image.load("balloon.jpg")

while True:
    screen.fill((0,0,0))

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos

    fox_rect = pygame.Rect(x, y, 100, 200)
    tree_rect = pygame.Rect(300, 200, 100, 100)

    screen.blit(fox_image, fox_rect)
    screen.blit(tree_image, tree_rect)
    pygame.display.flip()



    if fox_rect.colliderect(tree_rect):
         print("COLLIDE")
