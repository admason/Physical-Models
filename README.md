# Physical-Models
#### A library of mathematical models for the solution to physics problems.
## 1. **Ball_meets_sphere**
### **Build Status: Working model, under development**
##### The physics of a ball, or series of balls, dropping onto a sphere is simulated in this code.
[![bounce.jpg](https://i.postimg.cc/DZP0dSXY/bounce.jpg)](https://postimg.cc/jwCRRdvz)
###### The User may select the radius and elesticity of the falling ball as it collidfed with the sphere.
###### Generally the sphere should be significantly larger than the falling ball, however the User may feel free to experiment.
###### Once the criteria for the ball and sphere are defined, the User may click with the mouse on the screen to generate a ball, which will descend subject to gravitational for and collision with the sphere.
###### There is no limit to the quantity of balls which may be produced.

### **Tech** 
##### Coded with Python in Jupyter notebook with pygame, pymunk, sys, math. 
##### Import Library List: 
##### Libaries initiated with code as:
```
import pygame 
import sys
import pymunk 
import math as m
```

## **Code**
```
#### For one Static Ball


import pygame 
import sys
import pymunk 
import math as m


ball_size=int(input("Radius of falling ball? "))
ball_elast=int(input("Elasticity of falling ball, range [0,20]? "))
sphere_size=int(input("Radius of sphere? "))
sphere_elast=int(input("Elasticity static sphere, range [0,20]? "))


# create the physical body #uses floats
def create_apple(space,pos):
    body = pymunk.Body(1,100,body_type=pymunk.Body.DYNAMIC )
    body.position = pos
    shape = pymunk.Circle(body,ball_size)
    shape.elasticity=ball_elast/10
    space.add(body,shape)
    return shape

# draw the body in pygame #uses integers
def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),ball_size)
        #apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        #screen.blit(apple_surface,apple_rect)
        
# create another shape:
def static_ball(space):
    body = pymunk.Body(1,body_type=pymunk.Body.STATIC)
    body.position=(290,500)
    shape=pymunk.Circle(body,sphere_size)
    shape.elasticity=sphere_elast/10
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(0,0,0),(pos_x,pos_y),sphere_size)
    

    pygame.init() #initiating pygame
screen = pygame.display.set_mode((600,600)) # creates display surface
clock = pygame.time.Clock() #creates game clock
space = pymunk.Space() #create the space
space.gravity=(0,100) # give the space gravity for coordinates in (x,y)

#apple_surface = pygame.image.load('apple_red.png')
apples = []


balls=[]
balls.append(static_ball(space))

while True:   #Game Loop
    for event in pygame.event.get():  # checks user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))
            
    
    
    screen.fill((217,217,217)) #background colour
    draw_apples(apples)
    draw_static_ball(balls)
  
    
    space.step(1/150)           #size of update steps
    pygame.display.update()


```

## **Instructions**
#### Paste the code into a Jupyter notebook window.
#### Press SHIFT ENTER.
#### Click on screen


## **Future imporovements**
#### Allow for alternative shapes to fall.
#### Input via GUI
