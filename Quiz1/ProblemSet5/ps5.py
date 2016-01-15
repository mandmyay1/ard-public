# 6.00.2x Problem Set 5
# Graph optimization
# Finding shortest paths through MIT buildings
#

import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 

#
# Problem 2: Building up the Campus Map
#
# Before you write any code, write a couple of sentences here 
# describing how you will model this problem as a graph. 

# This is a helpful exercise to help you organize your
# thoughts before you tackle a big design problem!
#

def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    mapFile = open(mapFilename)
    g = WeightedDigraph()
    nodes = {}
    for line in mapFile:
        splitsies = line.split(" ")
        From = splitsies[0]
        To = splitsies[1]
        TotalDistance = splitsies[2]
        OutdoorDistance = splitsies[3]
        if From in nodes:
            fromNode = nodes[From]
        else:
            fromNode = Node(From)
            nodes[From] = fromNode
            g.addNode(fromNode)
        
        if To in nodes:
            toNode = nodes[To]
        else:
            toNode = Node(To)
            nodes[To] = toNode
            g.addNode(toNode)
            
        e = WeightedEdge(fromNode, toNode, TotalDistance, OutdoorDistance)
        g.addEdge(e)
    return g

# Problem 3: Finding the Shortest Path using Brute Force Search
#
# State the optimization problem as a function to minimize
# and what the constraints are
#
def getOutdoorsTo(digraph, start, end):
    edges = digraph.getOtherEdges()
    listToNodes = edges[start]
    for item in listToNodes:
        #item = [node, (totalDistance, outdoorDistance)]
        if item[0] == end:
            pair = item[1]
            return pair[1]
    return None

def getTotalDistTo(digraph, start, end):
    edges = digraph.getOtherEdges()
    listToNodes = edges[start]
    for item in listToNodes:
        #item = [node, (totalDistance, outdoorDistance)]
        if item[0] == end:
            pair = item[1]
            return pair[0]
    return None

def getPathDistance(digraph, path):
    total = 0
    if path is None: return 0
    startPointer = 0
    while startPointer+1 < len(path):
        p1 = path[startPointer]
        p2 = path[startPointer+1]
        total += getTotalDistTo(digraph, p1, p2)
        startPointer +=1
    return total

def findShortestPath(digraph, start, end, maxTotalDist, maxDistOutdoors, path = [], shortest=None):
    path =  path + [start]
    if start == end:
        return path
    for edge in digraph.childrenOf(start):
        node = edge[0]
        outDoors = getOutdoorsTo(digraph, start, node)
        totalDist = getTotalDistTo(digraph, start, node)
        if outDoors <= maxDistOutdoors and totalDist <= maxTotalDist:
            if node not in path:
                #if shortest == None or # len(path) < len(shortest):
                newPath = findShortestPath(digraph, node, end, maxTotalDist - totalDist, maxDistOutdoors - outDoors, path, shortest)
                if newPath != None:
                    pathDistance = getPathDistance(digraph, newPath)
                    shortestDistance = getPathDistance(digraph, shortest)
                    if shortest == None or pathDistance < shortestDistance:
                        shortest = newPath
    return shortest

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    shortestPath = findShortestPath(digraph, start, end, maxTotalDist, maxDistOutdoors)
    if shortestPath == None:
        raise ValueError
    return shortestPath

# map5 = WeightedDigraph()
# nodes = [Node("1"), Node("2"), Node("3"), Node("4"), Node("5")]
# map5.addNode(nodes[0])
# map5.addNode(nodes[1])
# map5.addNode(nodes[2])
# map5.addNode(nodes[3])
# map5.addNode(nodes[4])
# map5.addEdge(WeightedEdge(nodes[0], nodes[1], 5,2))
# map5.addEdge(WeightedEdge(nodes[2], nodes[4], 6,3))
# map5.addEdge(WeightedEdge(nodes[1], nodes[2], 20,10))
# map5.addEdge(WeightedEdge(nodes[1], nodes[3], 10,5))
# map5.addEdge(WeightedEdge(nodes[3], nodes[2], 2,1))
# map5.addEdge(WeightedEdge(nodes[3], nodes[4], 20,10))
# 
# print map5
# #print bruteForceSearch(map5, "1", "3", 17, 8)
# #print bruteForceSearch(map5, "1", "5", 23, 11)
# print bruteForceSearch(map5, "4", "5", 21, 11)
# #mitMap = load_map("mit_map.txt")
#bruteForceSearch(mitMap, "32", "56", 100000, 0)
#
# Problem 4: Finding the Shorest Path using Optimized Search Method
#
def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    shortestPath = findShortestPath(digraph, start, end, maxTotalDist, maxDistOutdoors)
    if shortestPath == None:
        raise ValueError
    return shortestPath


# Uncomment below when ready to test
#### NOTE! These tests may take a few minutes to run!! ####
if __name__ == '__main__':
    #Test cases
    mitMap = load_map("mit_map.txt")
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)
    print 'nodes', mitMap.nodes
    print 'edges', mitMap.edges


    LARGE_DIST = 1000000

    #Test case 1
    print "---------------"
    print "Test case 1:"
    print "Find the shortest-path from Building 32 to 56"
    expectedPath1 = ['32', '56']
    brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    dfsPath1 = directedDFS(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath1
    print "Brute-force: ", brutePath1
    print "DFS: ", dfsPath1
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath1 == brutePath1, expectedPath1 == dfsPath1)

    #Test case 2
    print "---------------"
    print "Test case 2:"
    print "Find the shortest-path from Building 32 to 56 without going outdoors"
    expectedPath2 = ['32', '36', '26', '16', '56']
    brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
    print "Expected: ", expectedPath2
    print "Brute-force: ", brutePath2
    print "DFS: ", dfsPath2
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath2 == brutePath2, expectedPath2 == dfsPath2)

    #Test case 3
    print "---------------"
    print "Test case 3:"
    print "Find the shortest-path from Building 2 to 9"
    expectedPath3 = ['2', '3', '7', '9']
    brutePath3 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    dfsPath3 = directedDFS(mitMap, '2', '9', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath3
    print "Brute-force: ", brutePath3
    print "DFS: ", dfsPath3
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath3 == brutePath3, expectedPath3 == dfsPath3)

    #Test case 4
    print "---------------"
    print "Test case 4:"
    print "Find the shortest-path from Building 2 to 9 without going outdoors"
    expectedPath4 = ['2', '4', '10', '13', '9']
    brutePath4 = bruteForceSearch(mitMap, '2', '9', LARGE_DIST, 0)
    dfsPath4 = directedDFS(mitMap, '2', '9', LARGE_DIST, 0)
    print "Expected: ", expectedPath4
    print "Brute-force: ", brutePath4
    print "DFS: ", dfsPath4
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath4 == brutePath4, expectedPath4 == dfsPath4)

    #Test case 5
    print "---------------"
    print "Test case 5:"
    print "Find the shortest-path from Building 1 to 32"
    expectedPath5 = ['1', '4', '12', '32']
    brutePath5 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    dfsPath5 = directedDFS(mitMap, '1', '32', LARGE_DIST, LARGE_DIST)
    print "Expected: ", expectedPath5
    print "Brute-force: ", brutePath5
    print "DFS: ", dfsPath5
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath5 == brutePath5, expectedPath5 == dfsPath5)

    #Test case 6
    print "---------------"
    print "Test case 6:"
    print "Find the shortest-path from Building 1 to 32 without going outdoors"
    expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
    brutePath6 = bruteForceSearch(mitMap, '1', '32', LARGE_DIST, 0)
    dfsPath6 = directedDFS(mitMap, '1', '32', LARGE_DIST, 0)
    print "Expected: ", expectedPath6
    print "Brute-force: ", brutePath6
    print "DFS: ", dfsPath6
    print "Correct? BFS: {0}; DFS: {1}".format(expectedPath6 == brutePath6, expectedPath6 == dfsPath6)

    #Test case 7
    print "---------------"
    print "Test case 7:"
    print "Find the shortest-path from Building 8 to 50 without going outdoors"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '8', '50', LARGE_DIST, 0)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr

    #Test case 8
    print "---------------"
    print "Test case 8:"
    print "Find the shortest-path from Building 10 to 32 without walking"
    print "more than 100 meters in total"
    bruteRaisedErr = 'No'
    dfsRaisedErr = 'No'
    try:
        bruteForceSearch(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        bruteRaisedErr = 'Yes'
    
    try:
        directedDFS(mitMap, '10', '32', 100, LARGE_DIST)
    except ValueError:
        dfsRaisedErr = 'Yes'
    
    print "Expected: No such path! Should throw a value error."
    print "Did brute force search raise an error?", bruteRaisedErr
    print "Did DFS search raise an error?", dfsRaisedErr
