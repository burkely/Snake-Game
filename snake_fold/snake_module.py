import pygame
import snake_fold.consts
import random

	
			
class Pellet():

	def __init__(self):
		#I dont want the pellets too close to the edge so Ill make sure their
		#starting pos is at least twice their size from the window edge
		#leaving at least a block sized distance between food pellets & edge
		self.pellet_size = snake_fold.consts.SNAKE_SIZE
		max_x_edge = snake_fold.consts.WINDOW_WIDTH - 2*self.pellet_size
		max_y_edge = snake_fold.consts.WINDOW_HEIGHT - 2*self.pellet_size
		
		x = random.randrange((2*self.pellet_size), max_x_edge, self.pellet_size)
		y = random.randrange((2*self.pellet_size), max_y_edge, self.pellet_size)
		self.pellet_pos = (x, y)
	
	def makeNewPellet(self):
		max_x_edge = snake_fold.consts.WINDOW_WIDTH - 2*self.pellet_size
		max_y_edge = snake_fold.consts.WINDOW_HEIGHT - 2*self.pellet_size
		
		x = random.randrange((2*self.pellet_size), max_x_edge, self.pellet_size)
		y = random.randrange((2*self.pellet_size), max_y_edge, self.pellet_size)
		self.pellet_pos = (x, y)
	
	def drawPellet(self, SCREEN):
		screen = SCREEN
		pygame.draw.rect(screen, snake_fold.consts.GREEN, (self.pellet_pos, (self.pellet_size, self.pellet_size)))
	

	
	
	

class completeSnake():
	def __init__(self, start_x, start_y, snake_size):
		#create a list/array to hold our complete snake
		#Initialize list to hold tuples for head/each body block & 
		#its direction
		self.snake = []
		
		#create snake head starting pos & snake size
		self.x = start_x
		self.y = start_y
		self.size = snake_size
		
		#Create vars to hold head snake attributes: head pos & direction
		self.head_pos = (start_x, start_y)
		self.head_curr_dir = snake_fold.consts.HEAD_DIR
		
		
		#append head snake attributes to end of list - 
		#List is empty so at top of the list now & will stay that way
		self.snake.append([self.head_pos, self.head_curr_dir])
		
	def createTail(self):	
		
		#if we only have the head so far..
		if len(self.snake)<2:
			last_block_pos, last_block_curr_dir = self.snake[0]
			new_block_curr_dir = last_block_curr_dir 
			new_block_next_dir = []
		else:
			last_block_pos, last_block_curr_dir, last_block_next_dir = self.snake[-1]
			new_block_curr_dir = last_block_curr_dir 
			new_block_next_dir = list(last_block_next_dir)
			
		last_x, last_y = last_block_pos
		
		#if we are travelling left make new block at left end of snake
		if last_block_curr_dir == 'left':
			new_block_pos = ((last_x+self.size), last_y)
		#if we are travelling right make new block at right end of snake
		elif last_block_curr_dir == 'right':
			new_block_pos = ((last_x-self.size), last_y)
		
		elif last_block_curr_dir == 'up':
			new_block_pos = (last_x, ((last_y+self.size)))
			
		elif last_block_curr_dir == 'down':
			new_block_pos = (last_x, (last_y-self.size))
		
		self.tail = [new_block_pos, new_block_curr_dir, new_block_next_dir]
		
		return self
		
	def addTail(self):
		#add tail to end of list (end of snake)
		self.snake.append(self.tail)
	
	def moveSnake(self):
		#move each snake part forward a length of self.
		#print self.snake
		
		for i, x in enumerate(self.snake):
			#the first 2 elements in the list item 'x' are current
			#position & current direction of the selected block
			#We access these first as all snake elements have
			#an x[0] and x[1]
			curr_pos = x[0]
			curr_direction = x[1]
			
			#Then we get the direction queue
			##if head - no direction queue
			if x == self.snake[0]:
				next_direction = None
				
			else: 
				next_direction = x[2]
			
			if next_direction:
				
			#If there is a queue check if block is ready to turn
			#ie at the place where the head turned
				next_pos, next_dir = next_direction[0]
				if curr_pos == next_pos:
				#if it is change its direction to the new direction 
					curr_direction = next_dir
					x[1] = curr_direction
				#and pop old direction change off the queue
					del next_direction[0]
				
			#Otherwise it's a head block/there's no queue so we 
			#want to continue moving without changing direction
		
			#now we move it
			curr_x, curr_y = curr_pos
			if curr_direction == 'left':
				new_pos = (curr_x-self.size, curr_y)
			elif curr_direction == 'right':
				new_pos = (curr_x+self.size, curr_y)
			elif curr_direction == 'up':
				new_pos = (curr_x, curr_y-self.size)
			elif curr_direction == 'down':
				new_pos = (curr_x, curr_y+self.size)
			#assign our new block back into list
			
			if x == self.snake[0]:
				new_block = [new_pos, curr_direction]
			else:
				new_block = [new_pos, curr_direction, next_direction]
			
			self.snake[i] = new_block	
	
	def turn(self):
		#Replace heads current direction with new one
		self.snake[0][1] = snake_fold.consts.HEAD_DIR
		
		#for every other snake block add the turn & turning
		#position to the list so it knows where and when to turn
		#Slicing list to exclude head (it has no dir list at i[2])
		
		for x, i in enumerate(self.snake):

			#to avoid doubles - ie debouncing - check if last element of queue
			#is equal to what we are trying to add
			if len(i)>2:
				if len(i[2])>0:
					last_dir_in_queue = i[2][-1]
				
					last_pos = last_dir_in_queue[0]
					
					if (last_pos!=snake_fold.consts.HEAD_POS):

						self.snake[x][2].append((snake_fold.consts.HEAD_POS, snake_fold.consts.HEAD_DIR))
					else:
						self.snake[x][2][-1] = (snake_fold.consts.HEAD_POS, snake_fold.consts.HEAD_DIR)
				
				else:
					self.snake[x][2].append((snake_fold.consts.HEAD_POS, snake_fold.consts.HEAD_DIR))
					

			
	
			
	def drawSnake(self, screen):
		for i in self.snake:
			x, y = i[0]
			pygame.draw.rect(screen, snake_fold.consts.BLUE, (x, y, self.size, self.size))
	
	def checkPelletCollision(self, pellet):
		#Accessing the snakes head position
		#The first bracket gives you the location of the tuple in your list. 
		#The second bracket gives you the location of the item in the tuple
		head_x, head_y = self.snake[0][0]
		food_x, food_y = pellet.pellet_pos
		
		#check if we are touching on any edge by comparing x,y co-ords &
		#looking for the head to be a distance of it & pellet size away from pellet
		if (food_x, food_y)==(head_x, head_y):
			return True
		else: return False
		
	
#GAme logic class goes here: check scores, bounces, touches etc LATER	
	
	"""def edge_bounce(self):
		if self.x <= (snake_fold.consts.left_edge + self.size):
			#turn and bounce back the to the right
			self.x = 2*self.size-self.x
			snake_fold.consts.head_direction = 'right'
			
			
		if self.x >= (snake_fold.consts.right_edge - self.size):
			#turn and bounce back the to the left
			self.x = 2*(width-self.size)-self.x
			snake_fold.consts.head_direction = 'left'
			
		if self.y <= (snake_fold.consts.top_edge + self.size):
			self.y = 2*self.size-self.y
			snake_fold.consts.head_direction = 'down'
			
		if self.y >= (snake_fold.consts.bottom_edge - self.size):
			self.y = 2*(height - self.size)-self.y 
			snake_fold.consts.head_direction = 'up'   """