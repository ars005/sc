import random
from numpy.random import randint

population=[[0,0,1,0,0,0,1],[0,1,0,0,0,0,0]]
population_fitness_dictionary={"0,0,1,0,0,0":1.245,"0,1,0,0,0,0,0":1.658}

def get_probablity_list():
  fitness=population_fitness_dictionary.values()
  total_fit=float(sum(fitness))
  relative_fitness=[f/total_fit for f in fitness]
  probablities=[sum(relative_fitness[:i+1])
          for i in range(len(relative_fitness))]
  return probablities

def roulette_wheel_pop(population,probablities,number):
  chosen=[]
  for n in range(number):
    r=random.random()
    for (i,individual) in enumerate(population):
      if r<=probablities[i]:
        chosen.append(individual)
        break
  return chosen

#tournament selection
def selection(pop,scores,k=2):
  #first random selection
  selection_ix=randint(len(pop))
  for ix in randint(0,len(pop),k-1):
    #check if better (e.g. perform a tournament)
    if scores[ix]<scores[selection_ix]:
      selection_ix=ix
  return pop[selection_ix]

def select_parents(population,scores):
  rank=[i for i in range(len(scores))]
  rank.sort(key=lambda x:scores[x],reverse=True)
  rank_prob=[((2*(len(scores))-i)/(2*len(scores))) for i in range(len(scores))]
  parent_indices=[]
  for i in range(2):
    random_number=random.uniform(0,1)
    for i,p in enumerate(rank_prob):
      if random_number< p:
        parent_indices.append(rank[i])
        break
  return [population[i] for i in parent_indices]

probablities = get_probablity_list()
print("Roulette Wheel Probabilities:", probablities)

# Run roulette wheel selection for 2 individuals
selected_individuals_roulette = roulette_wheel_pop(population, probablities, 2)
print("Selected Individuals (Roulette Wheel):", selected_individuals_roulette)

# Example usage of tournament selection (assuming scores are available)
# Replace with your actual scores for the population
scores = list(population_fitness_dictionary.values())
selected_individual_tournament = selection(population, scores)
print("Selected Individual (Tournament):", selected_individual_tournament)

# Example usage of rank-based selection (assuming scores are available)
selected_parents_rank = select_parents(population, scores)
print("Selected Parents (Rank-based):", selected_parents_rank)