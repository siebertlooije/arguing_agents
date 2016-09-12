import random
import numpy as np
from matplotlib import pyplot as plt

class negotiation_space():

	#add constructor to keep track of the agents

	w = 5
	h = 5

	def create_space(w,h):

		Space = [[0 for x in range(w)] for y in range(h)] 

		line_goal =  random.randint(0,w-1)
		final_goal = random.randint(0,h-1)		

		Space[line_goal][final_goal] = 10	#Optimal Goal
		
		return Space

	def set_Agents(Space,w,h):
		
		line_Trainer =  random.randint(0,w-1)
		final_Trainer = random.randint(0,h-1)

		line_President =  random.randint(0,w-1)
		final_President = random.randint(0,h-1)		

		Space[line_Trainer][final_Trainer] = 1 	
		Space[line_Trainer][final_Trainer] = 1

		Space[line_President][final_President] = 2
		Space[line_President][final_President] = 2

		return Space 	#Returns grid with different values for dif ag

	def negotiation_process(FullSpace):

		plt.matshow(FullSpace)
		plt.show()

	if __name__ == '__main__':
		
		Space = create_space(w,h)
		SpaceAgents = set_Agents(Space,w,h)
		negotiation_process(SpaceAgents)
		#plot(SpaceAgents)