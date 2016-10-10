"""Main Function that runs the whole simulation process"""

import random

from create_uniform_agents import *
from graph_representations import *
from geneticAlgorithm import *
from results import *

n_simulations = 25
extra_simulations = 10																																																																																																																																																																																																											
simulations_vector = []
extra_simulations_vector = []

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
	
	print "---------------------------------------------------------------"
	print "Which team do you want to simulate the negotiation process on?"
	print "---------------------------------------------------------------"
	print "1: Equally distributed members"
	print "2: President, CEO and Trainer negotiate"
	print "---------------------------------------------------------------"
	answer = raw_input("Your Choice:	")

	if answer == "1":

		ready_set = prepare_set(chromosomes_set,answer)
		Uniform_graph_representation()

		for i in xrange(0,n_simulations):

			simulations_vector.append(i)

			new_generation = create_next_generation(answer, ready_set)
			ready_set = prepare_set(new_generation, answer)
			print "Processing Generation:",i
			
			s = [item[1] for item in ready_set]
			global_score = score_keeper(s)
			global_scores.append(global_score)	

			if len(global_scores) != len(set(global_scores)):
				print "The Algotithm has converged in generation:", i
				break

		save_Uniform_results(simulations_vector,global_scores)
		convergence_plot(simulations_vector,global_scores)

	elif answer == "2":

		ready_set = prepare_set(chromosomes_set,answer)
		
		for i in xrange(0,n_simulations):

			simulations_vector.append(i)

			new_generation = create_next_generation(answer, ready_set)
			ready_set = prepare_set(new_generation,answer)
			print "Processing Generation:",i
			
			s = [item[1] for item in ready_set]
			global_score = score_keeper(s)
			global_scores.append(global_score)	
			
			if len(global_scores) != len(set(global_scores)):
				print "The Algorithm has converged in generation:", i
				last_generation = i

				for j in xrange(last_generation+1, (last_generation+extra_simulations)):

					extra_simulations_vector.append(j)

					new_generation = create_next_generation("1", ready_set)
					ready_set = prepare_set(new_generation, "1")
					
					s = [item[1] for item in ready_set]
					global_score = score_keeper(s)
					global_scores.append(global_score)
				
				break

		final_simulations = []
		final_simulations = simulations_vector + extra_simulations_vector

		save_PCT_results(final_simulations,global_scores)
		convergence_plot(final_simulations,global_scores)
