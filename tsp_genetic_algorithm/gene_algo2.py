import random
import time
from math import sqrt

class TSP_GENETIC_ALGORITHM():
    def __init__(self, coordinates, population_size, mutation_rate):
        self.coordinates = coordinates
        self.num_locations = len(self.coordinates)
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        
    def __generateIndividual(self):
        '''Creates an organism/indivdual from the coordinates of the locations'''
        organism_coordinates = self.coordinates.copy()                              # creates an copy of the coordinates of the locations
        organism = []
        
        # generates the coordinates of the individuals by randomly selecting coordinates and removing the added coordinates from the copy
        for coord in range(self.num_locations):
            organism.append(random.choice(organism_coordinates))
            organism_coordinates.remove(organism[coord])
            
        return organism
    
    def initialPopulation(self):
        '''Creates a population of candidate routes'''
        population = []
        for _ in range(self.population_size):
            organism = self.__generateIndividual()                                  # generates and individual/organism
            population.append(organism)                                             # appends the generated individual/organism into the population
            
        return population
    
    def evalFitness(self, organism_coord):
        '''Calculates and sums the distance between all the coordinates'''
        sum_results = 0
        for i in range(1, self.num_locations):
            x_diff = organism_coord[i][0] - organism_coord[i-1][0]                  # calculates the difference the x-coordinates
            y_diff = organism_coord[i][1] - organism_coord[i-1][1]              # calculates the difference the y-coordinates
            sum_results += sqrt(x_diff**2 + y_diff**2)                          # calculates and sums the calculated distance
        
        x_diff = organism_coord[self.num_locations-1][0] - organism_coord[0][0] # calculates the difference the x-coordinates
        y_diff = organism_coord[self.num_locations-1][1] - organism_coord[0][1] # calculates the difference the y-coordinates
        sum_results += sqrt(x_diff**2 + y_diff**2)                              # calculates and sums the calculated distance
        
        return sum_results
    
    def crossoverRandom(self, par1, par2):
        pass
    
    def crossover1Point(self, par1, par2):
        '''Performs 1 point crossover method (partially-mapped crossover) for the generation of the child'''
        offspring = self.num_locations * [None]
        point_sel = int(self.num_locations / 2)
        
        # copies the DNA material from parent 1 up to point_sel
        offspring[:point_sel] = par1[:point_sel]

        # copies the DNA material of parent 2 up to point_sel
        for i in range(point_sel):
            # search for the genetic material of parent 2 in the offspring and copy what does not exist already
            try:
                offspring.index(par2[i])                                        # find the index of element in index i of parent 2 in offspring
                continue
            except (ValueError):                                                # provided the value is non-existing in offspring
                x = par2.index(offspring[i])                                    # find the index in parent 2 where the offspring element is
                if x >= point_sel and offspring[x] == None:                     # if that element exists at a value above point_sel then assign it to offspring
                    offspring[x] = par2[i]
                else:                                                           # if the element at index x of parent 2 is located at some index below point_sel
                    while True:
                        x = par2.index(offspring[x])
                        if offspring[x] == None:
                            offspring[x] = par2[i]
                            break
                        
        # add the genetic material after point_sel from parent 2 into offspring
        for j in range(point_sel, self.num_locations):
            if offspring[j] == None:
                offspring[j] = par2[j]
        
        # introduces diverity to the offspring        
        offspring = self.__mutation(offspring)
                
        return offspring
    
    def crossover2Point(self, par1, par2):
        '''Performs 2 point crossover method (partially-mapped crossover) for the generation of the child'''
        offspring = self.num_locations * [None]
        point_sel0 = int(self.num_locations / 3)
        point_sel1 = self.num_locations - point_sel0
        
        # copies the DNA material from parent 1 between the two points
        offspring[point_sel0:point_sel1] = par1[point_sel0:point_sel1]
        
        # copies the genetic material of parent 2 to offspring between the selection points
        for i in range(point_sel0, point_sel1):
            try:
                offspring.index(par2[i])                                        # find the index of element in index i of parent 2 in offspring
                continue
            except(ValueError):
                x = par2.index(offspring[i])                                    # find the index in parent 2 where the offspring element is
                if x >= point_sel1 or x <= point_sel0 and offspring[x] == None:                          # if that element exists at a value outside the selection points then assign it to offspring
                    offspring[x] = par2[i]
                else:                                                           # if the element at index x of parent 2 is located at some index inside the selection points
                    while True:
                        x = par2.index(offspring[x])
                        if offspring[x] == None:
                            offspring[x] = par2[i]
                            break
        
        # copies the genetic material of parent 2 outside the selection points
        locs = [num for num in range(self.num_locations) if num < point_sel0 or num >= point_sel1]
        for j in locs:
            if offspring[j] == None:
                offspring[j] = par2[j]
        
        # introduces diverity to the offspring        
        offspring = self.__mutation(offspring)
        
        return offspring
    
    def __mutation(self, child_dna):
        '''Introduces diversity onto the child by making random changes to the DNA'''
        prob = 1.0 - self.mutation_rate
        for i in range(self.num_locations):
            probs = random.random()
            if probs >= prob:
                # selects a point to swap the genetic material at i with
                x_pos = [num for num in range(self.num_locations) if num != i]
                x = random.choice(x_pos)
                
                # swaps the two selected genetic materials
                x_tmp = child_dna[x]
                child_dna[x] = child_dna[i]
                child_dna[i] = x_tmp
                
        return child_dna
                    