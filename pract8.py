from collections import defaultdict
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import random
import pandas as pd
#load dataset

df=pd.read_excel(r"C:\Users\91892\Downloads\heart.xlsx")
print(df.describe())

#separate features (all column except 'target)
data_array = df.drop(columns=['target']).values #numpy array of features

#extract target as numpy array
target_array = df['target'].values
X=data_array
y=target_array
n_features = X.shape[1]

#standarized features
scaler = StandardScaler()
X = scaler.fit_transform(X)

#GA parameters
population_size = 10
n_generations = 10
mutation_rate = 0.1

#create initail population of binary feature masks
def initail_population(size, n_features):
    return [np.random.choice([0, 1], size=n_features)for _ in range(size)]

#fitness function: cross-validated accuracy
def fitness(individual):
    if np.count_nonzero(individual) == 0:
        return 0
    selected_features = X[:, individual == 1]
    model = LogisticRegression(max_iter=500)
    scores = cross_val_score(model, selected_features, y, cv=5)
    return scores.mean()

#selection : tournament selection
def select(population, fitness, k=3):
    selected = []
    for _ in range(len(population)):
        aspirants= random.sample(list(zip(population, fitness)), k)
        selected.append(max(aspirants, key=lambda x: x[1])[0])
        return selected
    
    #crossover :single point crossover
    def crossover(parent1, parent2):
        point = random.randint(1, n_features - 1)
        child1 = np.concatenate((parent1[:point], parent2[point:]))
        child2 = np.concatenate((parent2[:point], parent1[point:]))
        return child1, child2
    
    #mutation: flip bitis
    def mutate(individual, mutation_rate):
        for i in range(len(individual)):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]
                return individual
            
            #run genetic algorithm
            population = initail_population(population_size, n_features)
            print("Initial opulation:", population)

            best_fitness_per_gen = []

            for gen in range(n_generations):
                fitnesses = [fitness(ind) for ind in population]
                best_fitness = max(fitnesses)
                best_fitness_per_gen.append(best_fitness)

                print(f"Generation {gen}, Best Fitness:{best_fitness:.4f}")

                selected = select(population, fitness)
                next_population = []
                for i in range(0, population_size, 2):
                    p1, p2 = selected[i], selected[min(i+1, population_size-1)]
                    c1, c2 = crossover(p1,p2)
                    next_population.extend([mutate(c1, mutation_rate), mutate(c2, mutation_rate)])
                    population = next_population

                    #recompute fitness for all individuals in final population
                    final_fitness = [fitness(ind) for ind in population]

                    #get best individuqal (the one with the highest fitness)
                    best_index = np.argmax(final_fitness)
                    best_individual = population[best_index]

                    #use the original feature names form the dataset
                    #feature_names = data.features_name # form load_iris()

                    #get names of selected features 

                    feature_names = df.drop(columns=['target']).columns.tolist()
                    selected_features = np.array(feature_names)[best_individual == 1]

                    import matplotlib.pyplot as plt

                    plt.plot(best_fitness_per_gen, marker='o')
                    plt.title("Best fitness per generation")
                    plt.xlabel("Generation")
                    plt.ylabel("Best cross-validation accuracy")
                    plt.grid(True)
                    plt.show()

                    #get the best feature set
                    best_individual = population[np.argmax([fitness(ind) for ind in population])]
                    print(f"Selected features: {best_individual}, Total selected: {np.sum(best_individual)}")

                    print("Best individual(feature mask):", best_individual)
                    print("Selected features:", selected_features.tolist())
                    print("Total features selected:",np.sum(best_individual))



    