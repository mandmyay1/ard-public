def findDistinctDays(turbineData):
    retList = []
    for entry in turbineData:
        if retList.count( entry[1] ) is 0:
            retList.append( entry[1] )
    return retList

f = open("windfarm.dat",'r')
turbines = []
for line in f:
    broken = line.split()
    turbines.append(broken)
distinctDays = findDistinctDays(turbines)