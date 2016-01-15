import random, string, bisect

#https://www.reddit.com/r/dailyprogrammer/comments/40rs67/20160113_challenge_249_intermediate_hello_world/
allAvailableCharacters = string.ascii_letters+string.punctuation+" "
mutationProbability = 0.1
target = "Hello, World!"

def generateRandomWord(stringLength):
    return ''.join([random.choice(allAvailableCharacters) for _ in range(stringLength)])

def fitness(goal, current):
    currentFitness = 0
    for i in range(len(goal)):
        difference = ord(goal[i]) - ord(current[i])
        if difference < 0:
            difference *= -1
        currentFitness += difference
    return currentFitness

def minimumFitness(population):
    return sorted(population, key=lambda item: item[1])[1]
def averageFitness(population):
    return float(totalFitness(population))/len(population)
def totalFitness(population):
    return sum([item[1] for item in population])
def cdf(weights):
    total = sum(weights)
    result = []
    cumsum = 0
    for w in weights:
        cumsum += w
        result.append(cumsum / total)
    return result

def pickByFitness(population):
    maxWeight = population[-1][1]+1
    weights = [maxWeight-item[1] for item in population]
    weights = [float(i)/sum(weights) for i in weights]
    cdf_vals = cdf(weights)
    x = random.random()
    idx = bisect.bisect(cdf_vals, x)
    return idx
    
def mate(item1, item2):
    #need to implement random pick between the two items and then random mutation
    result = []
    for i in range(len(item1)):
        ch1 = item1[i]
        ch2 = item2[i]
        pick = random.choice([ch1,ch2])
        if random.random() < mutationProbability:
            pick = random.choice(allAvailableCharacters)
        result.append(pick)
    return ''.join(result)

def evolve(goal, population):
    amountToBreed = .2
    addToPopulation = []
    mated = []
    while float(len(mated))/(len(population)+len(mated)) < amountToBreed:
        idx1 = pickByFitness(population)
        mate1 = population.pop(idx1)
        mated.append(mate1)
        idx2 = pickByFitness(population)
        mate2 = population.pop(idx2)
        mated.append(mate2)
        addToPopulation.append(mate(mate1[0], mate2[0]))
    #items remaining in population should be replaced by the newly born
    while len(addToPopulation)>0:
        newItem = addToPopulation.pop()
        population.pop(-1)
        population.insert(0,(newItem, fitness(target, newItem)))
    population.extend(mated)
    return population




sizeOfPopulation = 100
population = []
for i in range(sizeOfPopulation):
    oneWord = generateRandomWord(len(target))
    population.append((oneWord, fitness(target, oneWord)))
    
population = sorted(population, key=lambda item: item[1])

avgFitness = averageFitness(population)
minFitness = minimumFitness(population)
generation = 0
while minFitness > 0 :#and generation < 1000:
    print generation, avgFitness, minFitness, population
    population = evolve(target, population)
    generation += 1
    population = sorted(population, key=lambda item: item[1])
    avgFitness = averageFitness(population)
    minFitness = population[0][1]

print generation, avgFitness, population