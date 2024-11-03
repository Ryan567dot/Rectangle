import pygame

pygame.init()

screen = pygame.display.set_mode(500,500)

pygame.display.pygame.display.set_caption("Catch me!")

#Rectangle

color = (128,0,128)

rec_x = 250
rec_y = 250
rec_w = 100
rec_h = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill((128,0,128))
    
    pygame.draw.rect(screen,color,(rec_x,rec_y,rec_w,rec_h))
    pygame.draw.circle(screen,(255,0,255),(0,0,255),(255,255,0),50)
    
    
pygame.display.flip()