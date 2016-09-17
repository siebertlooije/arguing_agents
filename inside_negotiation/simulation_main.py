import random

from create_teams import *
from geneticAlgorithm import *


if __name__ == '__main__':
	
	chromosomes_set = create_pool()
	scores = []

	ready_set = prepare_set(chromosomes_set)
	