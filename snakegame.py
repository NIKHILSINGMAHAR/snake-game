import turtle
import time
import random

delay=0.1
#set up the screen
wn=turtle.Screen()
wn.title("snake game by nikhil mahar")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)


#head
head=turtle.Turtle()
head.speed(0)
head.shape ("square")
head.color("black")
head.penup() # you can move turtle wihout leaving track 
head.goto(0,0)  #moves the turtle from the current position to location x,y along the shortest linear path betwen  two locations:
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]



 #functions
def go_up():
    if head.direction!="down":
       head_direction="up"
    
def go_down():
    if head.direction !="up":
       head_direction="down"
    
def go_left():
    if head.direction !="right":
       head_direction="left"
    
def go_right():
    if head.direction !="left ":
       head_direction="right"
     
     
    
def move():
   if head.direction=="up":
    y=head.ycor()
    head.sety(y+20)
    
   if head.direction=="down":
    y=head.ycor()
    head.sety(y-20)
    
   if head.direction=="left":
    x=head.xcor()
    head.setx(x-20)
    
    
   if head.direction=="right":
    x=head.xcor()
    head.setx(x+20)
    
#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")




#main game loop
while True :
   wn.update
   #check the collision with the border
   if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
       time.sleep(1)
       head.goto(0,0)
       head.direction="stop"
       
    #hide the segments
    
   for segment in segments:
       segment.goto(1000,1000)
       
       
       #clear the segments
       
       segments.clear()
        
       
   
   
   
   
   # check for a collision with the food

       if head.distance(food)< 20: #move the food to the random spot
        x = random.randint(-290,290)
        y = random.randint (-290,290)
        food.goto(x,y)
       
       #add a segments
       new_segment=turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.color("grey")
       new_segment.penup()
       segments.append(new_segment)
       #move the end segment first in reverse order
       for index in range (len(segments)-1,0,-1):
           x=segments[index-1].xcor()
           y=segments[index-1].ycor()
           segments[index].goto(x,y)
       #move segment 0to where the head is
       if len (segments)>0:
           x=head.xcor()
           y=head.ycor()
           segments[0].goto(x,y)          
       
   
   move()
   #check for the head collision with the body segments
   for segment in segments:
       if segment.distance (head)<20:
           time.sleep(1)
           head.goto(0,0)
           head.direction="stop"
           
            #hide the segments
    
   for segment in segments:
       segment.goto(1000,1000)
       
       
       #clear the segments
       
       segments.clear()
        
       
  
  
   time.sleep(delay)
    
   wn.mainloop()



