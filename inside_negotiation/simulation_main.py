import random

from create_teams import *
from geneticAlgorithm import *

n_simulations = 4

def score_keeper(scores):

	global_scores = []
	scores = []

	s = [item[1] for item in ready_set]

	for i in s:
		scores.append(i)
	
	tot = 0

	for i in scores:
		tot += i

	final_score = tot/len(scores)
	global_scores.append(final_score)

	for i in global_scores:
		print i

if __name__ == '__main__':
	
	chromosomes_set = create_pool()
	ready_set = prepare_set(chromosomes_set)
	
	print "First Generation of Agents", ready_set

	for i in xrange(0,n_simulations):

		new_generation = create_next_generation(ready_set)
		ready_set =prepare_set(new_generation)
		#print (new_generation)		