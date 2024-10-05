import timeit
import random

class Solucao:
    def __init__(self):
        self.comp = 0  # Comparison counter
        self.mov = 0    # Movement counter

    def indice_menor(self, arr):
        if len(arr) > 0:
            self.comp += 1  # Counting the comparison for finding minimum
            return arr.index(min(arr))

    def reset(self):
        self.comp = 0
        self.mov = 0

    # Problem setup
    def knapsack_genetic(self, v, w, capacity, n, population_size=200, num_generations=500, initial_mutation_rate=0.1, penalty_factor=10):
        
        # Fitness function with a penalty for exceeding capacity
        def fitness(individual):
            total_weight = sum(w[i] * individual[i] for i in range(n))
            total_value = sum(v[i] * individual[i] for i in range(n))
            self.mov += n  # Movement for calculating total weight and value
            if total_weight > capacity:
                self.comp += 1  # Comparison to check weight
                return total_value - penalty_factor * (total_weight - capacity)  # Penalty for exceeding capacity
            return total_value

        # Selection: choose the best individual from the population using tournament selection
        def selection(population, tournament_size=5):
            selected = random.sample(population, tournament_size)
            best_individual = max(selected, key=fitness)
            self.comp += tournament_size  # Comparisons for tournament selection
            return best_individual

        # Crossover: combine two parents to create two offspring (uniform crossover)
        def crossover(parent1, parent2):
            offspring1 = [parent1[i] if random.random() < 0.5 else parent2[i] for i in range(n)]
            offspring2 = [parent2[i] if random.random() < 0.5 else parent1[i] for i in range(n)]
            self.mov += n  # Movement for creating offspring
            return offspring1, offspring2

        # Mutation: randomly flip bits (items) in the individual's chromosome
        def mutate(individual, mutation_rate):
            for i in range(n):
                if random.random() < mutation_rate:
                    individual[i] = 1 - individual[i]  # Flip bit
                    self.mov += 1  # Movement for mutation
            return individual

        # Ensure the solution does not exceed capacity
        def repair(individual):
            total_weight = sum(w[i] * individual[i] for i in range(n))
            self.mov += n  # Movement for calculating weight
            while total_weight > capacity:
                idx_to_remove = random.choice([i for i in range(n) if individual[i] == 1])
                individual[idx_to_remove] = 0  # Remove item to reduce weight
                self.mov += 1  # Movement for removing item
                total_weight = sum(w[i] * individual[i] for i in range(n))
                self.mov += n  # Movement for recalculating weight
            return individual

        # Initialize population with random solutions
        def initialize_population():
            population = []
            for _ in range(population_size):
                individual = [random.randint(0, 1) for _ in range(n)]
                population.append(repair(individual))  # Ensure valid initial solutions
            return population

        # Run the genetic algorithm
        population = initialize_population()
        mutation_rate = initial_mutation_rate
        
        for generation in range(num_generations):
            new_population = []
            for _ in range(population_size // 2):
                parent1 = selection(population)
                parent2 = selection(population)
                offspring1, offspring2 = crossover(parent1, parent2)
                new_population.extend([repair(mutate(offspring1, mutation_rate)), repair(mutate(offspring2, mutation_rate))])  # Repair after mutation

            # Implement elitism: retain the best individual
            best_individual = max(population, key=fitness)
            new_population.append(best_individual)
            population = new_population
            
            # Reduce mutation rate over time (optional)
            mutation_rate *= 0.99

        # Find the best solution in the final population
        best_solution = max(population, key=fitness)
        return best_solution, fitness(best_solution)

    def alg_GEN(self, w: list, v: list):
        W = w.pop(0)  # First element is the total capacity
        n = v.pop(0)  # First element is the number of items
        self.mov += 1

        return self.knapsack_genetic(v, w, W, n)

    def main(self, w, v):
        antes = timeit.default_timer()
        saida = self.alg_GEN(w, v)
        depois = timeit.default_timer() - antes

        return saida, depois, self.comp, self.mov  # Return comparisons and movements
