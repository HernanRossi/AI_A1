import sys
from SearchTreeNode import SearchTreeNode

class IterativeDeepeningSearch:

    def __init__(self, start, goal, cityLocations, mapCitiesToNeighbours):
        self.startCity = start
        self.goalCity = goal
        self.numberOfNodesCreated = 0
        self.numberOfCitiesVisited = 0
        self.cityLocations = cityLocations
        self.mappingCitiesToConnectedNeighbours = mapCitiesToNeighbours
        self.allActionsTaken = []
        self.searchSolution = []
        self.visitedCities = []
        self.solutionFound = False

    def iterativeDS(self):
        # run DFS for current depth limit then increase and continue
        for depth in range(1, 100):
            # print('Starting a new iteration.')
            self.allActionsTaken = []
            self.searchSolution = []
            self.visitedCities = []
            result = self.depthLimit(depth)
            if result != 'Continue':
                return 'Solution Found'
        return 'No Solution Found'



    def depthLimit(self, limit):
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity], 0)
        stack = [startNode]
        numberOfNodesCreated = 1
        numberOfCitiesVisited = 0
        while stack:
            # print('making it into while', len(stack))
            city = stack.pop()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                numberOfCitiesVisited += 1
                # print('Visiting Goal', cityName)
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                self.numberOfNodesCreated = numberOfNodesCreated
                self.numberOfCitiesVisited = numberOfCitiesVisited
                self.solutionFound = True
                return 'Solution Found'
            if cityName not in visited:
                # print('Visiting ', city.getCity())
                if city.depth >= limit:
                    visited.append(cityName)
                    numberOfCitiesVisited += 1
                else:
                    visited.append(cityName)
                    numberOfCitiesVisited += 1
                    cityNeighbours = city.getNeighbours()
                    for neighbour in cityNeighbours:
                        newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                                 self.mappingCitiesToConnectedNeighbours[neighbour], city.depth + 1)
                        stack.append(newNode)
                        numberOfNodesCreated += 1
            else:
                # already visited
                continue
        # print('No solution Found.')
        return 'Continue'


