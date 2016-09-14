
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

	for i in n:
		score = compute_score(i)
		scores.append(score)
		agents.append(i)

	agents_pool = zip(agents,scores)
	sorted_pool = sorted(agents_pool,key = lambda t: t[1], reverse = True)

	print(sorted_pool)