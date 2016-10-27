import random

"""Script that models Agents as single Chromosomes. Every part
of the chromosome corresponds to a particular member of the team.
Every member has part of the knowledge (values) that is required
for satisfying an optimal fitness f(x) that corresponds to the 
reachment of an agreement.

This is the neutral team with equal impact of the members
"""

number_solutions = 20
n = 100

def part_President():
	
	p_impact = random.randint(1,n)
	binary_impact = '{0:08b}'.format(p_impact)

	return binary_impact

def part_Captain():
		
	c_impact = random.randint(1,n)
	binary_impact = '{0:08b}'.format(c_impact)

	return binary_impact

def part_Trainer():
	
	t_impact = random.randint(1,n)
	binary_impact = '{0:08b}'.format(t_impact)

	return binary_impact

def part_CEO():
	
	CEO_impact = random.randint(1,n)
	binary_impact = '{0:08b}'.format(CEO_impact)

	return binary_impact

def part_Supporters():
	
	s_impact = random.randint(1,n)
	binary_impact = '{0:08b}'.format(s_impact)

	return binary_impact

def create_Chromosome():
	
	president = part_President()
	captain = part_Captain()
	trainer = part_Trainer()
	ceo = part_CEO()
	supporters = part_Supporters()

	potential_team_solution = president+captain+trainer+ceo+supporters

	return potential_team_solution

def create_pool():
	
	initial_pool = []

	for i in xrange(0,number_solutions):
		team = create_Chromosome()
		initial_pool.append(team)

	return initial_pool


