#import seaborn as sns
from matplotlib import pyplot as plt

def save_Uniform_results(sim, scores):
	results = open('UniformTeamResults.txt', 'w')
	for i, j in zip(sim, scores):
		results.write("%i %i \n" % (i, j))

def save_PCT_results(sim,scores):
	results = open('PCTResults.txt', 'w')
	for i, j in zip(sim, scores):
		results.write("%i %i \n" % (i, j))

def save_Coop_results(sim,scores):
	results = open('CoopResults.txt', 'w')
	for i, j in zip(sim, scores):
		results.write("%i %i \n" % (i, j))

def convergence_plot(sim, scores):
	plt.xlabel('Number of Generations')
	plt.ylabel('Level of Disagreement')
	plt.title("Disagreement Graph")
	plt.plot(sim,scores)
	plt.show()
