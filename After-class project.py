import pygame
pygame.init()
screen.pygame.display.set_mode((400,500))
screen.pygame.display.set_caption(("This is a rectangle"))
done=False
while not done:
    for event in pygame.event.get():
        if event.type== pygame.QUIT():
            done=True
        pygame.draw.rect(screen , (0,345,200), pygame.rect(90,60,90,60))
        pygame.display.flip()
