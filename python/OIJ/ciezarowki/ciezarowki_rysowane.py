import pygame

pygame.init()
screen = pygame.display.set_mode([500, 500])
running = True
pygame.display.set_caption("Show Text")
font = pygame.font.Font("freesansbold.ttf", 12)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (50, 250), (450, 250))
    for i in range(50, 490, 40):
        text = font.render(f"{i}", True, (0, 0, 0), (255, 255, 255))
        textRect = text.get_rect()
        pygame.draw.line(screen, (0, 0, 0), (i, 255), (i, 245))
        textRect.center = (i + 1, 240)
        screen.blit(text, textRect)
    pygame.display.flip()


pygame.quit()
