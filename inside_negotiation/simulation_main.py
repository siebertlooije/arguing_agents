import random

from create_teams import *
from geneticAlgorithm import *


if __name__ == '__main__':
	
	chromosomes_set = create_pool()
	scores = []

	s = evaluate_set(chromosomes_set)