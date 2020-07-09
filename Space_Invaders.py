import turtle, math, random, winsound

#Setting up the primary screen for the game
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
#Gridding the position
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
#Register the shapes
wn.register_shape("invader.gif")
wn.register_shape("player.gif")

#Sound effects
winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
winsound.PlaySound("laser.wav", winsound.SND_ASYNC)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#Set the score to 0
score = 0

#Dra the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#Creating the player
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#Movement of character
playerspeed = 30
bulletspeed = 10
#Moving player to the left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < - 290:
        x = - 290
    player.setx(x)

#Moving player right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 290:
        x = 290
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs change of state
    global bulletstate
    if bulletstate == "ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"

        #Move the bullet to just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

#Create the players weapon
bullet = turtle.Turtle()
bullet.color("pink")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

#Define weapon state
#ready - ready to fire
#fire - bulet is firing
bulletstate = "ready"

#Choose a num of enemies
number_of_enemies = 5
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
    #Create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("white")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-250, 200)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
#keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#create enemy
enemy = turtle.Turtle()
enemy.color("white")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2
#main game loop
while True:
    for enemy in enemies:
        #Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

    #Moving enemy back and forth

        if enemy.xcor() > 280:
            #To move all enemies down
            for enmy in enemies:
                y = enmy.ycor()
                y -= 40
                enmy.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #Move all enemies down
            for enmy in enemies:
                y = enmy.ycor()
                y -= 40
                enmy.sety(y)
            #Change enemy direction
            enemyspeed *= -1

        # Check for a collision between the bullet and the enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            # Reset Bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, - 400)
            # Reset the enemy
            enemy.setposition(-200, 250)

            # Reset Enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #Update the score
            score += 10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if isCollision(player, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

wn.mainloop()

