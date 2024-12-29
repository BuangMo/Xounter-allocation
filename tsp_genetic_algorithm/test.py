import gene_algo2 as GA
import random
import time

def main():
    coord = [[100, 300], [200, 130], [300, 500], [500, 390], [700, 300], [900, 600], [800, 950], [600, 550], [350, 550], [270, 350]]
    population_size = 10
    mut_rate = 0.05                                                             # can be 2-5%
    fitness_tmp = 100.0**2
    generation = 0
    fitness_flag = 0
    
    start = time.time()
    obj = GA.TSP_GENETIC_ALGORITHM(coord, population_size, mut_rate)
    population = obj.initialPopulation()
    
        
    while True:
        # sorts the population in ascending order using the fitness of individuals
        org_fitness = [obj.evalFitness(x) for x in population]                  # gets the fitness of each individual
        res = zip(org_fitness, population)                                      # combines the two lists into a single iterable
        res = sorted(res, key=lambda result:result[0])                          # sorts the iterable using fitness of individuals
        org_fitness, population = zip(*res)                                     # extracts the population that was sorted using the fitness
            
        # break from the loop if the target has been found
        if org_fitness[0] < fitness_tmp:
            fitness_tmp = org_fitness[0]
            fitness_flag = 0
        else:
            fitness_flag += 1
            if fitness_flag == 20: break
        
        # perform Elitism, meaning 10% of the fittest individuals of this generation continue to the next
        new_population = []
        '''x = int((population_size * 10)/100)
        new_population.extend(population[:x])
        
        # 90% of the offspring is porduced by 50% of the fittest individuals in the population
        x = int((population_size * 90)/100)'''
        for _ in range(population_size):
            parent1 = random.choice(population[:int(population_size/2)])
            parent2 = random.choice(population[:int(population_size/2)])
            offspring = obj.crossover1Point(parent1, parent2)
            new_population.append(offspring)
            
        population = new_population
        print(f"Generation {generation}: Str = {population[0]}, Fitness: {org_fitness[0]}")
        generation += 1
        
    stop = time.time()
    print(f"Generation {generation}: Str = {population[0]}, Fitness: {org_fitness[0]}")
    print(f"\ntime: {stop - start} s")        
        
if __name__ == '__main__': 
	main()
