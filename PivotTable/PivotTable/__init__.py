import functools

def findDistinctTurbines(turbineData):
    retList = []
    for entry in turbineData:
        if retList.count( entry[0] ) is 0:
            retList.append( entry[0] )
    return retList

f = open("windfarm.dat",'r')
t = []
for line in f:
    broken = line.split()
    t.append(broken)
turbines = findDistinctTurbines(t)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
t2 = {}
for turbine in turbines:
    filt = [(item[1],int(item[2])) for item in t if item[0] == turbine]
    for day in days:
        f2 = [amt[1] for amt in filt if amt[0] == day]
        total = functools.reduce(lambda x,y: x+y, f2)
        if turbine in t2.keys():
            d = t2[turbine]
            d[day] = total
            t2[turbine] = d
        else:
            t2[turbine] = {day:total}
        
print( "Tower\t" + functools.reduce(lambda x,y: x+y, [day + "\t" for day in days]) )
for turbine in sorted(t2.keys()):
    s = turbine + "\t"
    for day in days:
        s += str(t2[turbine][day]) + "\t"
    print( s )