import seaborn as sns
from matplotlib import pyplot as plt

def convergence_plot(sim, scores):

	plt.xlabel('Number of Generations')
	plt.ylabel('Level of Disagreement')
	plt.title("Disagreement Graph")
	plt.plot(sim,scores)
	plt.show()
