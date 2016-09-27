"""Main Function that runs the whole simulation process"""

import random

from create_uniform_agents import *
from geneticAlgorithm import *
from results import *

n_simulations = 20
simulations_vector = []

for i in xrange(0,n_simulations):
	simulations_vector.append(i)

def score_keeper(s):

	scores = []

	for i in s:
		scores.append(i)
	
	tot = 0

	for i in scores:
		tot += i

	return tot/len(scores)
	
if __name__ == '__main__':

	global_scores = []
	
	chromosomes_set = create_pool()
	ready_set = prepare_set(chromosomes_set)
	
	print "---------------------------------------------------------------"
	print "Which team do you want to simulate the negotiation process on?"
	print "---------------------------------------------------------------"
	print "1: Equally distributed members"
	print "2: Second Option"
	print "---------------------------------------------------------------"
	answer = raw_input("Your Choice:	")

	if answer == "1":

		for i in xrange(0,n_simulations):

			new_generation = create_next_generation(ready_set)
			ready_set = prepare_set(new_generation)
			print "Processing Generation:",i
			
			s = [item[1] for item in ready_set]
			global_score = score_keeper(s)
			global_scores.append(global_score)	

		save_Uniform_results(simulations_vector,global_scores)
		convergence_plot(simulations_vector,global_scores)
