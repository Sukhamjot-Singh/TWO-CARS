import pygame
import random
import math


pygame.init()

screen = pygame.display.set_mode((600,1000))

#backimg = pygame.image.load("back.jpg")


car1_img = pygame.image.load("car.png")
car1_x = 161
car1_y = 800

car2_img = pygame.image.load("car.png")
car2_x = 311
car2_y = 800


car1_initial = "right"
car2_initial = "left"



circle1img = pygame.image.load("circle.png")
circle1_x = random.choice([42,192])
circle1_y = random.randint(0,150)

circle2img = pygame.image.load("circle2.png")
circle2_x = random.choice([492,342])
circle2_y = random.randint(0,150)

square1img = pygame.image.load("square.png")
square1_x = random.choice([42,192])
square1_y = circle1_y - 400


square2img = pygame.image.load("square2.png")
square2_x = random.choice([492,342])
square2_y = circle2_y - 400

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def car1(x,y):
	screen.blit(car1_img,(x,y))
def car2(x,y):
	screen.blit(car2_img,(x,y))
def circle1(x,y):
	screen.blit(circle1img,(x,y))
def circle2(x,y):
	screen.blit(circle2img,(x,y))
def square1(x,y):
	screen.blit(square1img , (x,y))
def square2(x,y):
	screen.blit(square2img , (x,y))
def colliding(x1,x2,y1,y2):
	distance = math.sqrt( math.pow((x1 - x2) , 2) + math.pow ((y1 - y2) , 2) )
	if distance < 40:
		return True
def showscore(x,y):
	scorevalue = font.render("Score : " + str(score), True , (0,255,0))
	screen.blit(scorevalue , (x,y))
def gameover(x,y):
	overtext = font.render("GAMEOVER",True , (0,255,0))
	replay = font.render("PRESS ENTER TO RESTART",True,(0,255,0))
	screen.blit(overtext , (x,y))
	screen.blit(replay , (x-100,y + 100))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN:
				main()

def main():
  vel = 100
  car1_x = 161
  car1_y = 800
  car2_x = 311
  car2_y = 800
  car1_initial = "right"
  car2_initial = "left"
#circle1img = pygame.image.load("circle.png")
  circle1_x = random.choice([42,192])
  circle1_y = random.randint(0,150)

#circle2img = pygame.image.load("circle2.png")
  circle2_x = random.choice([492,342])
  circle2_y = random.randint(0,150)


#square1img = pygame.image.load("square.png")
  square1_x = random.choice([42,192])
  square1_y = circle1_y - 400


#square2img = pygame.image.load("square2.png")
  square2_x = random.choice([492,342])
  square2_y = circle2_y - 400
  score = 0
  font = pygame.font.Font('freesansbold.ttf', 32)

  running = True

  while running:

	screen.fill((100,100,150))
	# screen.blit(backimg, (0,0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				if car2_initial is "left":
					vel = 150
					car2_x += vel
					car2_initial = "right"
				else:
					vel =-150
					car2_x += vel
					car2_initial = "left"
			if event.key == pygame.K_SPACE:
				if car1_initial is "right":
					vel = -150
					car1_x += vel
					car1_initial = "left"
				else:
					vel = 150
					car1_x += vel
					car1_initial = "right"

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				vel = 0
			if event.key == pygame.K_RIGHT:
				vel = 0



	pygame.draw.line(screen,(255,255,255),(300,1000),(300,0),10)
	pygame.draw.line(screen,(255,255,255),(150,1000),(150,0),5)
	pygame.draw.line(screen,(255,255,255),(450,1000),(450,0),5)


	car1(car1_x,car1_y)
	car2(car2_x,car2_y)

	if (circle1_y >= 900) or (circle2_y >= 900):
		gameover(200,250)
		circle1_y = 1200
		circle1_x = 1200
		circle2_y = 1200
		square1_x = 1200
		square2_x = 1200


	if(square1_y >= 900):
		square1_y = circle1_y - 400
		square1_x = random.choice([42,192])
	if(square2_y >= 900):
		square2_y = circle2_y - 400
		square2_x = random.choice([342,492])



	circle1_y += 1
	circle2_y += 1

	square1_y += 1
	square2_y += 1

	# list1 = [circle1(circle1_x,circle1_y),square1(square1_x,square1_y)]
	# list2 = [circle2(circle2_x,circle2_y),square2(square2_x,square2_y)]
	# random.choice(list1)()
	# random.choice(list2)()

	circle1(circle1_x,circle1_y)
	circle2(circle2_x,circle2_y)

	square1(square1_x,square1_y)
	square2(square2_x,square2_y)


	if colliding(car1_x,circle1_x,car1_y,circle1_y):
		score += 1
		circle1_y = random.randint(0,150)
	 	circle1_x = random.choice([42,192])

	if colliding(car2_x,circle2_x,car2_y,circle2_y):
		score += 1
		circle2_y = random.randint(0,150)
	 	circle2_x = random.choice([342,492])

	if colliding(car1_x,square1_x,car1_y,square1_y) or colliding(car2_x,square2_x,car2_y,square2_y):
		gameover(200,250)
		circle1_y = 1200
		circle1_x = 1200
		square1_x = 1200
		square2_x = 1200




	showscore(10,10)





	pygame.display.update()
main()
