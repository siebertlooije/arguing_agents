import random

"""The Genetic Algorithm is seen as the way the agents exchange
part of their knowledge in the format of bits in order to satisfy
a f(x) = agreement (the idea is to get a chromosome with only 0s)
Right now only one particular tyoe if Agent is created that can be 
changed on every bit, however we will represent mulitple ones where only 
part of their structure can be modified according to the type of abstract
argument that we want to simulate
"""

truncation_value_PTC = 80
truncation_value_single = 80

def PTC_crossover(parent_1, parent_2):	#Only President, Trainer and CEO have an impact on the negotiation process

	p1 = list(parent_1)
	p2 = list(parent_2)

	knowledge_impact_1_1 = p1[0:8]
	knowledge_impact_1_2 = p1[16:32]

	no_knowledge_impact_1_1 = p1[8:16]
	no_knowledge_impact_1_2 = p1[32:40]

	knowledge_impact_2_1 = p2[0:8]
	knowledge_impact_2_2 = p2[16:32]
	
	no_knowledge_impact_2_1 = p1[8:16]
	no_knowledge_impact_2_2 = p1[32:40]

	c1 = knowledge_impact_2_1 + no_knowledge_impact_1_1 + knowledge_impact_2_2 + no_knowledge_impact_1_2
	c2 = knowledge_impact_1_1 + no_knowledge_impact_2_1 +knowledge_impact_1_2 + no_knowledge_impact_2_2
		
	child1 = ''.join(c1)
	child2 = ''.join(c2)

	return child1, child2

def Uniform_single_crossover(parent_1, parent_2): 

	n = 10	#Bits to exchange that can have an impact on 
			#every part of the Chromosome ---> They all 
			#attack eachother

	c1 = list(parent_1)
	c2 = list(parent_2)

	for i in xrange(0,n):
		replace = random.randint(0,len(c1)-1)
		val = c2[replace]
		c1[replace] = val
		
	child1 = c1

	for i in xrange(0,n):
		replace = random.randint(0,len(c2)-1)
		val = c1[replace]
		c2[replace] = val
		
	child1 = ''.join(c1)
	child2 = ''.join(c2)

	return child1, child2

def random_mutation(generation):	#1% mutation rate
	
	index = random.randrange(len(generation))
	gene_to_mutate = generation[index]

	list_gene_to_mutate = list(gene_to_mutate)

	index = random.randint(0,len(list_gene_to_mutate)-1)
		
	for i, j in enumerate(list_gene_to_mutate):
		if i == index:
			if j == "0":
				list_gene_to_mutate[i] = 1
			elif j == "1":
				list_gene_to_mutate[i] = 0
			else:
				raise Exception("Chromosome is not supported!")
		
	mutated_gen = ''.join(str(e) for e in list_gene_to_mutate)
	generation[index] = mutated_gen
	
	return generation

def create_next_generation(answer, pool):	#New Generation of Agents is computed

	new_generation = []
	individual_chromosomes = [item[0] for item in pool]

	if answer == "1":

		for i in xrange(0, len(individual_chromosomes)-1):
			child_1, child_2 = Uniform_single_crossover(individual_chromosomes[i], individual_chromosomes[i+1])
			new_generation.append(child_1)
			new_generation.append(child_2)

		final_generation = random_mutation(new_generation)

	elif answer == "2":
		
		for i in xrange(0, len(individual_chromosomes)-1):
			child_1, child_2 = PTC_crossover(individual_chromosomes[i], individual_chromosomes[i+1])
			new_generation.append(child_1)
			new_generation.append(child_2)

		final_generation = random_mutation(new_generation)
		
	else:
		raise Exception("The option you chose does not exist!")

	return final_generation

def filter_set_single(population): 	#We keep only the fittest Agents fot simulation+1

	percentage_to_keep = (len(population)*truncation_value_single)/100
	new_set = population[-percentage_to_keep:]

	return new_set

def filter_set_PTC(population): 	#We keep only the fittest Agents fot simulation+1

	percentage_to_keep = (len(population)*truncation_value_PTC)/100
	new_set = population[-percentage_to_keep:]

	return new_set

def compute_score(chromo):	#Preparation of the pool

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

def prepare_set(solution_set, answer):	#Preparation of the pool

	scores = []
	agents = []

	for i in solution_set:
		score = compute_score(i)
		scores.append(score)
		agents.append(i)

	agents_pool = zip(agents,scores)
	sorted_pool = sorted(agents_pool,key = lambda t: t[1], reverse = True)

	if answer == "1":
		filtered_set = filter_set_single(sorted_pool)
	elif answer == "2":
		filtered_set = filter_set_PTC(sorted_pool)
	else:
		raise Exception("The option you chose does not exist!")

	return filtered_set
