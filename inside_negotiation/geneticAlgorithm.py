import random

truncation_value = 80

def single_crossover(parent_1, parent_2):

	n = 3	#Bits to exchange that can have an impact on 
			#every part of the Chromosome ---> They all 
			#attack eachother

	parent_1 = ''.join(str(e) for e in parent_1)
	parent_2 = ''.join(str(e) for e in parent_2)
		
	for i in xrange(0,n):

		bit_to_replace = random.randint(0,len(parent_1)-1)
		#print "Bit to replace", bit_to_replace

		cross_over_1_1 = parent_1[bit_to_replace]
		cross_over_1_2 = parent_2[bit_to_replace]

		child1 = parent_1.replace(parent_1[bit_to_replace], cross_over_1_2)
		child2 = parent_2.replace(parent_2[bit_to_replace], cross_over_1_1)

	#print "End of the breeding"
	print "Child 1", child1
	print "Child 2", child2
	
	return child1, child2

def create_next_generation(pool):

	new_generation = []
	individual_chromosomes = [item[0] for item in pool]

	for i in xrange(0, len(individual_chromosomes)-1):
		child_1, child_2 = single_crossover(individual_chromosomes[i], individual_chromosomes[i+1])
		new_generation.append(child_1)
		new_generation.append(child_2)

	return new_generation

def filter_set(population):

	percentage_to_keep = (len(population)*truncation_value)/100
	new_set = population[-percentage_to_keep:]

	return new_set

def compute_score(chromo):

	president_score = chromo[0:8]
	captain_score = chromo[8:16]
	trainer_score = chromo[16:24]
	ceo_score = chromo[24:32]
	supporters_score = chromo[32:40]

	president_score = int(president_score,2)
	captain_score = int(captain_score,2)
	trainer_score = int(trainer_score,2)
	ceo_score = int(ceo_score,2)
	supporters_score = int(supporters_score,2)

	chromosome_score = president_score+captain_score+trainer_score+ceo_score+supporters_score

	return chromosome_score

def prepare_set(solution_set):

	scores = []
	agents = []

	for i in solution_set:
		score = compute_score(i)
		scores.append(score)
		agents.append(i)

	agents_pool = zip(agents,scores)
	sorted_pool = sorted(agents_pool,key = lambda t: t[1], reverse = True)

	filtered_set = filter_set(sorted_pool)

	return filtered_set
