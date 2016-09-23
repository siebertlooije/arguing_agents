"""Main Function that runs the whole simulation process"""
"""TODO make classes out of all these scripts"""

import random

from create_teams import *
from geneticAlgorithm import *
from plots import *

n_simulations = 5
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
	
	print "First Generation of Agents", ready_set

	for i in xrange(0,n_simulations):

		new_generation = create_next_generation(ready_set)
		ready_set =prepare_set(new_generation)
		print "Processing Generation:",i
		
		s = [item[1] for item in ready_set]
		global_score = score_keeper(s)
		global_scores.append(global_score)	

	for i in global_scores:
		print(i)
		
	convergence_plot(simulations_vector,global_scores)
