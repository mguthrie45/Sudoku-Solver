from random import *

def generate_soln():	
	base  = 3
	side  = base*base

	# pattern for a baseline valid solution
	def pattern(r,c): 
		return (base*(r%base)+r//base+c)%side

	# randomize rows, columns and numbers (of valid base pattern)
	def shuffle(s): 
		return sample(s,len(s)) 
	rBase = range(base) 
	rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
	cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
	nums  = shuffle(range(1,base*base+1))

	# produce board using randomized baseline pattern
	board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

	return board

def generate_board():
	board = generate_soln()

	percentage = uniform(.25, 0.6)
	print(percentage, "\n")

	for i in range(len(board)):
		for j in range(len(board[i])):
			choice = random()
			if choice <= percentage:
				board[i][j] = 0

	return board


