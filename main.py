import pygame 
pygame.init()

screen=pygame.display.set_mode((400,300))
clock=pygame.time.Clock()
bird=pygame.image.load("Flappy-bird-clone/Bird.png")
bird_rect=bird.get_rect(topleft=(0,0))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
    
    screen.blit(bird_rect,bird)
    pygame.display.update()
    clock.tick(60)

    

    