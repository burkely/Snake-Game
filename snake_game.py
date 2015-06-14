import pygame
import snake_fold.snake_module
import snake_fold.consts
import sys


#initialize our screen size & title 
screen_size = (snake_fold.consts.WINDOW_WIDTH, snake_fold.consts.WINDOW_HEIGHT)
pygame.display.set_caption('SNAKE')
screen = pygame.display.set_mode(screen_size)

#create clock object to monitor FPS
clk = pygame.time.Clock()



# ---------- Main Program Loop --------- #

pygame.init

#get the game crackin'
SNAKE_SIZE = 25
START_X = 50
START_Y = 50

my_snake = snake_fold.snake_module.completeSnake(START_X, START_Y, SNAKE_SIZE)
food_pellet = snake_fold.snake_module.Pellet()

#list to hold change direction queue

running = True

while running:
	# ----- Main Event Handling Loop ---- #
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			snake_fold.consts.HEAD_POS = (my_snake.snake[0][0])
			
			if event.key == pygame.K_LEFT:
				snake_fold.consts.HEAD_DIR = snake_fold.consts.LEFT
				my_snake.turn()
				
			elif event.key == pygame.K_RIGHT:
				snake_fold.consts.HEAD_DIR = snake_fold.consts.RIGHT
				my_snake.turn()
			
			elif event.key == pygame.K_UP:
				snake_fold.consts.HEAD_DIR = snake_fold.consts.UP
				my_snake.turn()
				
			elif event.key == pygame.K_DOWN:
				snake_fold.consts.HEAD_DIR = snake_fold.consts.DOWN
				my_snake.turn()
				
	
				
	# ------ Game Logic Goes here ------ #
	
	my_snake.moveSnake()
	#check if we touched food:
	if my_snake.checkPelletCollision(food_pellet):
		#if true make new tail & add it to end of snake
		#chained methods execute left to right
		my_snake.createTail().addTail()
		#increase score
		food_pellet.makeNewPellet()
	
	
	# -------- Drawing code -------- #
	screen.fill(snake_fold.consts.BLACK)
	
	food_pellet.drawPellet(screen)
	my_snake.drawSnake(screen)
	pygame.display.flip()
	
	# tick() will return # of ms since previous call
	#passing FPS argument limits the runtime speed of game to 
	#that many fPS
	clk.tick(snake_fold.consts.FPS)
	
# close the window and uninitialize all pygame modules
pygame.quit()