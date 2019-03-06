import random

class Genetic():    
    def __init__(self, phrase, population_size, mutation_rate, characters):
        self.phrase = phrase
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.characters = characters
        self.population = []

    def run(self):
        self.__create_initial_pool()
        generations = 0

        # loop through each generation
        while True:       
            found = False
            for phrase in self.population:
                print(phrase)
                if phrase == self.phrase:  
                    found = True              
                    break   
            print("generations: ", generations)
            if found:
                break

            mating_pop = self.__mating_population()         
            self.__reproduction(mating_pop)        
            generations += 1
    
    # randomly create the initial population
    def __create_initial_pool(self):               
        # loop for number of phrases in population
        for _ in range(self.population_size):
            phrase = ''
            # create a phrase
            for _ in range(len(self.phrase)):
                num = random.randint(0,len(self.characters)-1)
                phrase += self.characters[num]

            #self.population.append("".join(str(x) for x in pool_phrase))        
            self.population.append(phrase)

    # fitness factor
    # based of number of matched characters divided by total characters
    def __fitness(self, pool_phrase):
        fitness = 0
        total = len(self.phrase)
        for i in range(len(self.phrase)):
            if self.phrase[i] == pool_phrase[i]:
                fitness += 1
        return fitness/total

    # create a mating pool 
    # just adds phrase from original pool to new mating pool
    #       based on percentage of fitness factor out of 100
    #       example: fitness factory of .50 will add that phrase
    #                   50 times to mating pool
    def __mating_population(self):
        mating_pop = []

        for p in self.population:
            fit = self.__fitness(p)
            # print(fit)
            for _ in range(int(fit*100)):
                mating_pop.append(p)
        
        return mating_pop

    # use the mating pool to create a child poplation
    def __reproduction(self, mating_pop):               
        new_population = []

        # loop for population size
        for _ in range(self.population_size):
            # randomly get the mom and date from mating pool
            mom = mating_pop[random.randint(0,len(mating_pop)-1)]
            dad = mating_pop[random.randint(0,len(mating_pop)-1)]

            # randomly get index to split mom and dad for combination
            slice_point = random.randint(0,len(mom))
            # combine mom and dad based on split point
            child = mom[:slice_point] + dad[slice_point:]
            
            # time to mutate the child - three eyeballs or four legs
            mutated_child = ''
            for char in child:
                # get random number
                mut = random.randint(1,100)
                # see if random number is less than or equal to mutation rate
                if mut <= self.mutation_rate*100:
                    # mutate character - grab random characther from char array
                    mutated_child += self.characters[random.randint(0,len(self.characters)-1)]
                else:
                    mutated_child += char
            
            new_population.append(mutated_child)
        
        self.population = new_population

        
def main():
    phrase = 'genetic programming is the bomb'
    population_size = 3000
    mutation = .01
    characters = 'abcdefghijklmnopqrstuvwxyz '
    genetic = Genetic(phrase, population_size, mutation, characters)
    genetic.run()

if __name__ == "__main__":
    main()