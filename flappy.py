import pygame
import random
import webbrowser
pygame.init()
pygame.mixer.init()
gamewindow=pygame.display.set_mode((400,500))
pygame.display.set_caption("FLAPPY BIRD")
icon=pygame.image.load('icon.png').convert_alpha()
pygame.display.set_icon(icon)

yellow=(255,255,0)
white=(255,255,255)
green=(34,139,34)
red=(255,0,0)
black=(0,0,0)
blue=(30,144,255)
green=(50,205,50)

#velocity_y=0

exit=False
background=pygame.image.load('bg.jpg')
background=pygame.transform.scale(background,(400,500)).convert_alpha()
back=pygame.image.load('bg_3.jpg')
back=pygame.transform.scale(back,(270,120)).convert_alpha()
base=pygame.image.load('base.png')
base=pygame.transform.scale(base,(400,100)).convert_alpha()
bird=pygame.image.load('brd.png')
bird=pygame.transform.scale(bird,(35,35)).convert_alpha()
birdw=pygame.image.load('birdd.png')
birdw=pygame.transform.scale(birdw,(50,50)).convert_alpha()
birds=pygame.image.load('birdd_1.png')
birds=pygame.transform.scale(birds,(70,70)).convert_alpha()
title=pygame.image.load('Caption.PNG')
title=pygame.transform.scale(title,(200,80))
head=pygame.image.load('Caption_1.PNG')
head=pygame.transform.scale(head,(220,100))
over=pygame.image.load('over.PNG')
over=pygame.transform.scale(over,(220,100))
key=pygame.image.load('key.png')
key=pygame.transform.scale(key,(35,35)).convert_alpha()
me=pygame.image.load('prince.png')
me=pygame.transform.scale(me,(120,120)).convert_alpha()
pipe1=pygame.image.load('pipe.png')
pipe1=pygame.transform.scale(pipe1,(70,220)).convert_alpha()
pipe2=pygame.transform.rotate(pygame.image.load('pipe.png').convert_alpha(),180)
pipe2=pygame.transform.scale(pipe2,(70,180)).convert_alpha()
google=pygame.image.load('GOOGLE.png')
google=pygame.transform.scale(google,(50,50)).convert_alpha()
#pipe_w=50
score=0
best_score=0

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,30,bold=True)
fonts=pygame.font.SysFont("Arial",25,bold=True)

def welcome():
    exit=False
    bird_x=20
    bird_y=260
    while not exit:
        for events in pygame.event.get():
            if(events.type==pygame.QUIT):
                exit=True     
            if(events.type==pygame.MOUSEBUTTONDOWN):
                if(110<=mouse[0]<=180 or 350<=mouse[1]<=380):
                    pygame.mixer.music.load('swoosh.mp3')
                    pygame.mixer.music.play()
                    start()
                if(150<=mouse[0]<=270 or 10<=mouse[1]<=130):
                    webbrowser.open("https://www.instagram.com/divyanshu_1807gupta/")
        
        bird_x+=4
        if(bird_x==400):
            bird_x=0

        gamewindow.blit(background,(0,0))
        gamewindow.blit(me,(150,10))
        gamewindow.blit(title,(100,160))
        gamewindow.blit(birdw,(310,170))
        gamewindow.blit(bird,(bird_x,bird_y))
        pygame.draw.rect(gamewindow,red,(110,350,70,30))
        mouse=pygame.mouse.get_pos()
        text=font.render("Start",True,black)
        gamewindow.blit(text,(122,355))
        pygame.draw.rect(gamewindow,red,(225,350,70,30))
        text=font.render("Score",True,black)
        gamewindow.blit(text,(233,355))
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit() 

def start():
    exit=False
    while not exit:
        for events in pygame.event.get():
            if(events.type==pygame.QUIT):
                exit=True     
            if(events.type==pygame.KEYDOWN):
                if(events.key==pygame.K_UP):
                    pygame.mixer.music.load('swoosh.mp3')
                    pygame.mixer.music.play() 
                    gameloop()

            if(events.type==pygame.MOUSEBUTTONDOWN):
                if(300<=mouse[0]<=400 or 330<=mouse[1]<=3700):
                    webbrowser.open("https://flappy-bird.io/")
    
        gamewindow.blit(background,(0,0))
        gamewindow.blit(head,(100,50))
        gamewindow.blit(birdw,(120,150))
        gamewindow.blit(birds,(190,160))
        text=font.render("PRESS",True,black)
        gamewindow.blit(text,(130,265))
        mouse=pygame.mouse.get_pos()
        gamewindow.blit(key,(210,255))
        text=fonts.render("For more games click here ",True,red)
        gamewindow.blit(text,(30,345))
        gamewindow.blit(google,(300,330))
        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()

def gameloop():
    global score 
    score=0
    game_over=False
    exit=False
    bird_x=100
    pipe_x=250
    pipe_x1=450
    pipe2_y=random.randint(-30,0)
    pipe1_y=random.randint(220,300)
    pipe2_y1=random.randint(-100,0)
    pipe1_y1=random.randint(220,300)
    bird_y=200
    while not exit:
        #pipe_x=random.randint(200,500)
        #pipe_h=random.randint(50,100)
        if(game_over==True):
            pygame.mixer.music.load('hit.mp3')
            pygame.mixer.music.play()
            final()

        else:
            for events in pygame.event.get():
                if(events.type==pygame.QUIT):
                    exit=True        
                if(events.type==pygame.KEYDOWN):
                    #if(events.key==pygame.K_RIGHT):
                    #    bird_x+=10
                    #if(events.key==pygame.K_LEFT):
                    #    bird_x-=10
                    if(events.key==pygame.K_UP):
                        pygame.mixer.music.load('wing.mp3')
                        pygame.mixer.music.play()
                        bird_y-=20
                    #if(events.key==pygame.K_DOWN):
                    #    bird_y+=20

            
            if((pipe_x-30<=bird_x<=pipe_x+70 and pipe1_y-30<=bird_y<=pipe1_y+220) 
               or (pipe_x-30<=bird_x<=pipe_x+70 and pipe2_y<=bird_y<=pipe2_y+175) 
               or (pipe_x1-30<=bird_x<=pipe_x1+70 and pipe1_y1-30<=bird_y<=pipe1_y1+220) 
               or (pipe_x1-30<=bird_x<=pipe_x1+70 and pipe2_y1<=bird_y<=pipe2_y1+175)):
                game_over=True


            pipe_x-=4
            if(pipe_x<0):
                pipe_x=400
                pipe2_y=random.randint(-100,0)
                pipe1_y=random.randint(220,300)
            pipe_x1-=4
            if(pipe_x1<0):
                pipe_x1=400
                pipe2_y1=random.randint(-100,0)
                pipe1_y1=random.randint(220,300)

            
            if(70<=bird_x-pipe_x<=73 or 70<=bird_x-pipe_x1<=73):
                pygame.mixer.music.load('point.mp3')
                pygame.mixer.music.play()
                score+=1

            head1=[]
            head1.append(pipe_x)
            head1.append(pipe1_y)
            head3=[]
            head3.append(pipe_x1)
            head3.append(pipe1_y1)
            lower_pipe=[]
            lower_pipe.insert(0,head1)
            lower_pipe.insert(1,head3)

            head2=[]
            head2.append(pipe_x)
            head2.append(pipe2_y)
            head4=[]
            head4.append(pipe_x1)
            head4.append(pipe2_y1) 
            upper_pipe=[]
            upper_pipe.insert(0,head2)
            upper_pipe.insert(1,head4)
            bird_y+=3

            #bird_y-=1 
            #gamewindow.fill(white)
            gamewindow.blit(background,(0,0))
            gamewindow.blit(bird,(bird_x,bird_y))
            for x,y in lower_pipe:
                gamewindow.blit(pipe1,(x,y))
            for x,y in upper_pipe:
                gamewindow.blit(pipe2,(x,y))
            text=fonts.render("Score: ",True,red)
            gamewindow.blit(text,(10,10))
            text=fonts.render(str(score),True,red)
            gamewindow.blit(text,(80,10))
            gamewindow.blit(base,(0,400))

            #pygame.draw.rect(gamewindow,yellow,(bird_x,bird_y,20,20)) 
            #pygame.draw.rect(gamewindow,green,(pipe_x,0,pipe_w,pipe_h))
            #pygame.draw.rect(gamewindow,green,(pipe_x,300,pipe_w,pipe_h))  
            pygame.display.update()
            clock.tick(30)

    pygame.quit()
    quit() 

def final():
    global score
    global best_score
    if(best_score<score):
        best_score=score
    exit=False
    while not exit:
        for events in pygame.event.get():
            if(events.type==pygame.QUIT):
                exit=True        
            if(events.type==pygame.MOUSEBUTTONDOWN):
               if(110<=mouse[0]<=180 and 350<=mouse[1]<=380):
                    pygame.mixer.music.load('swoosh.mp3')
                    pygame.mixer.music.play()
                    welcome()
               if(225<=mouse[0]<=300 and 350<=mouse[1]<=380):
                    pygame.mixer.music.load('swoosh.mp3')
                    pygame.mixer.music.play()
                    webbrowser.open("https://web.whatsapp.com/")

        gamewindow.blit(background,(0,0))
        gamewindow.blit(over,(95,50))
        gamewindow.blit(back,(70,170))
        text=font.render("Score",True,black)
        gamewindow.blit(text,(100,200))
        text=font.render(str(score),True,black)
        gamewindow.blit(text,(120,230))
        text=font.render("Best Score",True,black)
        gamewindow.blit(text,(210,200))
        text=font.render(str(best_score),True,black)
        gamewindow.blit(text,(250,230))
        mouse=pygame.mouse.get_pos()
        pygame.draw.rect(gamewindow,red,(110,350,70,30))
        text=font.render("OK",True,black)
        gamewindow.blit(text,(128,356))
        pygame.draw.rect(gamewindow,red,(225,350,75,30))
        text=font.render("Share",True,black)
        gamewindow.blit(text,(233,355))
        pygame.display.update()
    pygame.quit()
    quit()

welcome()


