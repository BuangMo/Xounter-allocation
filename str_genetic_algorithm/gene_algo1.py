import random
import time

class GENETIC_ALGORITHM():
    def __init__(self, pop_size, target):
        self.population_size = pop_size
        self.target = target
        self.target_len = len(self.target)
        self.dna = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!\"#%&/()=?@${[]}"
        
    def create_organism(self):
        '''creates a string that is the length of the target string'''
        organism = [random.choice(self.dna) for _ in range(self.target_len)]
        return organism
    
    def initialPopulation(self):
        '''Creates the initial population of organisms'''
        population = []
        for _ in range(self.population_size):
            organism = self.create_organism()
            population.append(organism)
            
        return population
    
    def evalFitness(self, organism):
        '''Calculates fitness of the individual - how it compares to the target'''
        fitness = 0
        for organism_element, target_element in zip(organism, self.target):
            if organism_element != target_element: fitness += 1
            
        return fitness
    
    def createOffspring(self, par1, par2):
        '''Mixes and matches the DNA of the two parents to produce an offspring'''
        offspring = []
        
        for dna_par1, dna_par2 in zip(par1, par2):
            probability = random.random()
            
            # assign DNA to the child
            if probability < 0.45:                                  # assigns DNA of parent 1 if probability < 45%
                offspring.append(dna_par1)
            elif probability < 0.90:                                # assigns DNA of parent 2 if probability < 90%
                offspring.append(dna_par2)
            else:                                                   # assigns random DNA (mutation) if probability > 90%
                offspring.append(random.choice(self.dna))
                
        return offspring
    
def main():
    population_size = 100
    target_str = "Sarah Baartman"
    generation = 0
    
    obj = GENETIC_ALGORITHM(population_size, target_str)            # creates an instance of the class
    start = time.time()
    # creates an initial population
    population = obj.initialPopulation()
    
    while True:
        # sorts the population in ascending order using the fitness of individuals
        org_fitness = [obj.evalFitness(x) for x in population]      # gets the fitness of each individual
        res = zip(org_fitness, population)                          # combines the two lists into a single iterable
        res = sorted(res, key=lambda result:result[0])              # sorts the iterable using fitness of individuals
        org_fitness, population = zip(*res)                         # extracts the sorted population and fitness
            
        # break from the loop if the target has been found
        if org_fitness[0] == 0:
            break
        
        # 50% of the fittest individuals to produce the new generation
        new_population = []
        for _ in range(population_size):
            parent1 = random.choice(population[:int(population_size/2)])
            parent2 = random.choice(population[:int(population_size/2)])
            new_population.append(obj.createOffspring(parent1, parent2))
    
        population = new_population
        print(f"Generation {generation}: Str = {population[0]}, Fitness: {org_fitness[0]}")
        generation += 1
       
    stop = time.time()
    print(f"Generation {generation}: Str = {population[0]}, Fitness: {org_fitness[0]}")
    print(f"\ntime: {stop - start} s")
if __name__ == '__main__': 
	main()