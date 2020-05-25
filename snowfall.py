import pygame
import random

BLACK=[0,0,0] #RGB
WHITE=[255,255,255]# RGB
#DESIGNING A SMALL SCREEN
SIZE=[400,400] #WIDTH & HEIGHT

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("My animation of Snow Flakes")

#Create an empty list
snow_list=[]

#loop 50 times and add a snow flake in a random x,y position
for i in range(100):
    x=random.randrange(0,400)
    y=random.randrange(0,400)
    snow_list.append([x,y])


clock = pygame.time.Clock()
#pygame for monitoring time, keeping a track of time, 1/1000 seconds -> 1 millisecond
#resolution

done=False

while not done:  #basically while true

    for event in pygame.event.get(): #get captures the last event clicked
        if event.type == pygame.QUIT: #when the user closes the window
            done = True #we are done so we exit




    screen.fill(BLACK)

    #process each snowflake from the list
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1

        #if the snowflake has moved outside your screen, bottom
        if snow_list[i][1]>400:
            y=random.randrange(-50,-10)
            snow_list[i][1]=y

            x=random.randrange(0,400)
            snow_list[i][1]=x


    pygame.display.flip() #for display on screen, changes only a small area on the screen

    clock.tick(20)

pygame.quit() #deactivate from pygame




