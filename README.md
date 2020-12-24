# Physical-Models
#### A library of mathematical models for the solution to physics problems.
## 1. **Ball_meets_sphere** 
##### Ball_meets_sphere.ipynb
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


## 2. **Cascade** 
##### Cascade.ipynb
### **Build Status: Working model, under development**
##### The physics of a ball, or series of balls, dropping onto a lattice of sphere is simulated in this code.
##### The bottom row may be arranged as a catchment row, onto which the balls will pile up. To acheive this set "Size of Static rock" = 25
[![bounce.jpg](https://i.postimg.cc/DZP0dSXY/bounce.jpg)](https://postimg.cc/jwCRRdvz)
###### The User may select the radius and elesticity of the falling ball as it collidfed with the sphere.
###### Generally the sphere should be significantly larger than the falling ball, however the User may feel free to experiment, try Size of Falling Rock = 3, "Size of Statis rock" = 25
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

### **Code**
```
#### for more than one static ball


import pygame 
import sys
import pymunk 
import math as m

bal=int(input("Size of falling rock?"))
pt=int(input("Size of static rocks?"))
fpt=float(pt)

# create the physical body #uses floats

def create_apple(space,pos):
    body = pymunk.Body(1,10,body_type=pymunk.Body.DYNAMIC )
    body.position = pos
    shape = pymunk.Circle(body,bal)
    shape.elasticity = 0.5
    shape.friction = 0.9   
    space.add(body,shape)
    return shape

# draw the body in pygame #uses integers
def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen,(50,200,100),(pos_x,pos_y),bal)
        #apple_rect = apple_surface.get_rect(center = (pos_x,pos_y))
        #screen.blit(apple_surface,apple_rect)

# create static array of balls:
def static_ball(space,pos):
    body = pymunk.Body(1,body_type=pymunk.Body.STATIC)
    body.position=pos
    shape=pymunk.Circle(body,pt)
    shape.elasticity=0.9
    space.add(body,shape)
    return shape

def draw_static_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        pygame.draw.circle(screen,(25,25,200),(pos_x,pos_y),pt)
        #pygame.draw.ellipse(screen,(50,200,100),(pos_x,pos_y),pt)
# create catchment row
def static_row(space,pos):
    body = pymunk.Body(1,body_type=pymunk.Body.STATIC)
    body.position=pos
    shape=pymunk.Circle(body,pt)
    shape.elasticity=0.9
    space.add(body,shape)
    return shape

def draw_static_row(rows):
    for row in rows:
        pos_x = int(row.body.position.x)
        pos_y = int(row.body.position.y)
        pygame.draw.circle(screen,(25,25,100),(pos_x,pos_y),fpt)
    
     
 
    


pygame.init() #initiating pygame
screen = pygame.display.set_mode((600,600)) # creates display surface
clock = pygame.time.Clock() #creates game clock
space = pymunk.Space() #create the space
space.gravity=(0,100) # give the space gravity for coordinates in (x,y)
#apple_surface = pygame.image.load('apple_red.png')

apples = []
balls=[]
rows=[]

# First Row
balls.append(static_ball(space,(50,200)))
balls.append(static_ball(space,(150,200)))
balls.append(static_ball(space,(250,200)))
balls.append(static_ball(space,(350,200)))
balls.append(static_ball(space,(450,200)))
balls.append(static_ball(space,(550,200)))

# Second Row
balls.append(static_ball(space,(100,300)))
balls.append(static_ball(space,(200,300)))
balls.append(static_ball(space,(300,300)))
balls.append(static_ball(space,(400,300)))
balls.append(static_ball(space,(500,300)))

# Third Row
balls.append(static_ball(space,(50,400)))
balls.append(static_ball(space,(150,400)))
balls.append(static_ball(space,(250,400)))
balls.append(static_ball(space,(350,400)))
balls.append(static_ball(space,(450,400)))

# fourth row
balls.append(static_ball(space,(100,500)))
balls.append(static_ball(space,(200,500)))
balls.append(static_ball(space,(300,500)))
balls.append(static_ball(space,(400,500)))
balls.append(static_ball(space,(500,500)))


# Fith Row
balls.append(static_row(space,(100,600)))
balls.append(static_row(space,(200,600)))
balls.append(static_row(space,(300,600)))
balls.append(static_row(space,(400,600)))
balls.append(static_row(space,(500,600)))

# Fouth Row
balls.append(static_row(space,(50,600)))
balls.append(static_row(space,(150,600)))
balls.append(static_row(space,(250,600)))
balls.append(static_row(space,(350,600)))
balls.append(static_row(space,(450,600)))
balls.append(static_row(space,(550,600)))


while True:   #Game Loop
    for event in pygame.event.get():  # checks user input
        if event.type == pygame.QUIT: # input to close the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            apples.append(create_apple(space,event.pos))
            
    
    
    screen.fill((0,0,27)) #background colour
    draw_apples(apples)
    draw_static_ball(balls)
    draw_static_row(rows)
    
    space.step(1/200)           #size of update steps
    pygame.display.update()


```
