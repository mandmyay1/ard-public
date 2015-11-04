import pylab
from builtins import map

def parseData():
    inFile = open("julyTemps.txt")

    highs = []
    lows = []
    
    for line in inFile:
        fields = line.split(" ")
        #if len(fields) < 3 or not fields[0].isdigit():
        if not fields[0].isdigit() or len(fields) < 3:
            #print(fields)
            pass
        else:
            highs.append(int(fields[1]))
            lows.append(int(fields[2]))
    return (lows, highs)


def producePlot(lowTemps, highTemps):
    diffTemps = list(map( (lambda x,y : x-y), highTemps, lowTemps))
    pylab.plot(range(1,32), diffTemps)
    pylab.title("Day by Day Ranges in Temperature in Boston in July 2012")
    pylab.xlabel("Days")
    pylab.ylabel("Temperature Ranges")
    pylab.show()
    

(lows, highs) = parseData()
producePlot(lows, highs)