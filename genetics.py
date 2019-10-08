class Genetics:
    # Parameters for controlling the genetics
    # Current itteration of the genetics
    run = 0
    # Current generation
    generation = 0
    # Number of individuals that will be selected to breed (default = 0.1)
    selection_rate = 0.05                                                          
    # Chance that a gene will mutate (default = 0.01)
    mutation_rate = 0.01
    # Size of the population (default = 100)
    population_size = 100
    # Range of weights (default = 1.0)
    random_weight_range = 1.0
    # Number of generations to run (default = 100)
    max_generations = 100
    # List that stores the average score of every generation
    generationScores = []
    # Generation max scores
    generationMaxScores = []

    def __init__(self):
        # Get the initial neural network model
        self.model = NeuralNetwork(input_shape=(16), action_space=4, custom=True).model
        pg.init()
        # Create the initial population
        population = self.create_inital_population()

        self.run_genetics(population)

    def create_initial_population(self):
        """
        Creates the initial population for the model to work off of
        """

        # Will be a list of weights
        population = []
        # Initial weights from the model
        initialWeights = self.model.get_weights()
        # Randomly set weight values
        for i in range(0, self.population_size):
            individual = initialWeights
            for a in range(0, len(initialWeights)):
                for b in range(0, len(initialWeights[a])):
                    for c in range(0, len(initialWeights[a][b])):
                        initialWeights[a][b][c] = self.getRandomWeight()
            population.append(copy.deepcopy(individual))
        
        return population

    def run_genetics(self):
         """
        Runs the simulation
        """
        while self.generation < self.max_generations:
            # Scores for all of the populations
            scores = {}

            # Run game for all members
            for i in range(0, self.population_size):
                self.model.set_weights(population[i])
                scores.update(self.gameCycle(self.model, i))
            
            print(scores)
            self.generationScores.append(self.average(scores))
            
            self.generation += 1

            # Kill the bottom 90% of the population
            parents = self.killWeak(population, scores)

            if self.save_best:
                self.saveBest(parents[0])

            # Breed new ones from the top 10% of performers
            newPopulation = self.breedToFull(parents)
            population = newPopulation
            #newPopulation = self.mutate(newPopulation)
            print("Generation: {}".format(self.generation))
        # Ending things
        print(self.generationScores)
        print(self.generationMaxScores)
        x = range(0, self.max_generations)

        fig, ax = plt.subplots()
        ax.plot(x, self.generationScores, x, self.generationMaxScores)
        ax.set(xlabel='generation', ylabel='avg score', title='Generations Over Time')
        ax.grid()
        if self.save_graph:
            fig.savefig("graph{}.png".format(self.overallRun))
        plt.show()