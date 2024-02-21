import pygame 
from random import randint
import math

pygame.init()

def make_pipes(pipes):
    global add_pipe

    pipe_surf=pygame.image.load("Pipes.png")
    pipe_surf=pygame.transform.scale(pipe_surf,(90,500))

    random_val=randint(100,300)
    pipe1_rect=pipe_surf.get_rect(bottomleft=(500,random_val))
    pipe2_rect=pipe_surf.get_rect(topleft=(500,(random_val+150)))

    if add_pipe:
        pipes.append(pipe1_rect)
        pipes.append(pipe2_rect)
        add_pipe=False
    
    for pipe in pipes:
        pipe.x-=2
    
    for pipe in pipes:
        if pipe.topleft[1]<0:
           rotaed_pipe_surf=pygame.transform.rotate(pipe_surf,180)
           screen.blit(rotaed_pipe_surf,pipe)
        else:    
           screen.blit(pipe_surf,pipe)
        
    for index,a in enumerate(pipes):
        if a.x<-100:
            del pipes[index]
    

def drawing_bird(bird_rect):
    global gravity

    gravity+=1.2
    bird_rect.y+=gravity
    if bird_rect.bottomleft[1] >=600:
        bird_rect.bottom=600

    screen.blit(bird,bird_rect)

def sky_scroling():
    global sky_scrool
    sky_scrool-=1.5
    for i in range(0,sky_tiles+1):
        screen.blit(sky_surf,(i*sky_width+sky_scrool,0))

    if abs(sky_scrool)>sky_width:
        sky_scrool=0
    
    
def ground_scroling():
    global ground_scroll
    ground_scroll-=2

    for i in range(0,sky_tiles+1):
        screen.blit(ground_surf,(i*sky_width+ground_scroll,500))
    if abs(ground_scroll)>ground_width:
        ground_scroll =0


screen=pygame.display.set_mode((500,600)) #500
clock=pygame.time.Clock()
bird=pygame.image.load("Bird.png")
bird=pygame.transform.scale(bird,(100,100))
bird_rect=bird.get_rect(center=(200,250))

gravity=0

pipes=[]
add_pipe=False

sky_surf=pygame.image.load('pxfuel.jpg')
sky_surf=pygame.transform.scale(sky_surf,(500,500))
ground_surf=pygame.image.load("pxfuel (copy).jpg")
ground_surf=pygame.transform.scale(ground_surf,(500,200))

# sky_rect=sky_surf.get_rect(topleft=(0,0))
ground_rect=ground_surf.get_rect(topleft=(0,500))

pipe_spawn=pygame.USEREVENT +1
pygame.time.set_timer(pipe_spawn,2000)

#scrolling
sky_width=sky_surf.get_width()
ground_width=ground_surf.get_width()
sky_tiles=math.ceil(500/sky_width)
ground_tiles=math.ceil(500/ground_width)

ground_scroll=0
sky_scrool=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                gravity=-12
        if event.type==pipe_spawn:
            add_pipe=True

    sky_scroling()
    make_pipes(pipes)
    ground_scroling()
    drawing_bird(bird_rect)

    
    pygame.display.update()
    clock.tick(60)