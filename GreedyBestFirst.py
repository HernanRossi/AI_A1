import math
from SearchTreeNode import SearchTreeNode

class GreedyBestFirst:

    def __init__(self, start, goal, cityLocations, mapCitiesToNeighbours):
        self.startCity = start
        self.goalCity = goal
        self.cityLocations = cityLocations
        self.mappingCitiesToConnectedNeighbours = mapCitiesToNeighbours
        self.allActionsTaken = []
        self.searchSolution = []
        self.numberOfNodesCreated = 0
        self.numberOfCitiesVisited = 0
        self.solutionFound = False
        self.cities = ['A', 'B', 'C', 'D', 'E', 'F',
                       'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R',
                       'S', 'T', 'U', 'V', 'W', 'X',
                       'Y', 'Z']
        self.mapCitiesToDistanceToGoalEuclideanDist = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
            'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
            'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
            'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
            'Y': 0, 'Z': 0
        }
        self.mapCitiesToDistanceToGoalManhattanDist = {
            'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
            'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
            'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0,
            'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
            'Y': 0, 'Z': 0
        }
        self.calcAllCityDistToGoalEuclidean()
        self.calcAllCityDistanceToGoalManhattanDistance()


    def greedyBestFirstSearchEuclidean(self):
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        stack = [startNode]
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        while stack:
            city = stack.pop()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
                print('Visiting Goal', cityName)
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                self.solutionFound = True
                return self.searchSolution
            if cityName not in visited:
                # print('Visiting ', city.getCity())
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                mapCurrentNeighbourToHeuristic = {}
                for neighbour in cityNeighbours:
                    mapCurrentNeighbourToHeuristic[neighbour] = self.mapCitiesToDistanceToGoalEuclideanDist[neighbour]

                while len(mapCurrentNeighbourToHeuristic) > 0:
                    addClosestToGoalNeighbour = max(mapCurrentNeighbourToHeuristic, key=mapCurrentNeighbourToHeuristic.get)
                    # print(addClosestToGoalNeighbour)
                    # print(self.mapCitiesToDistanceToGoalEuclideanDist[addClosestToGoalNeighbour])
                    del mapCurrentNeighbourToHeuristic[addClosestToGoalNeighbour]
                    newNode = SearchTreeNode(addClosestToGoalNeighbour, self.cityLocations[addClosestToGoalNeighbour], city,
                                             self.mappingCitiesToConnectedNeighbours[addClosestToGoalNeighbour])
                    stack.append(newNode)
                    self.numberOfNodesCreated += 1

            else:
                # already visited
                continue
            # print('No solution Found.')
        return []

    def greedyBestFirstSearchNoHeuristic(self):
            self.allActionsTaken = []
            self.searchSolution = []
            self.solutionFound = False
            visited = []
            startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                       self.mappingCitiesToConnectedNeighbours[self.startCity])
            stack = [startNode]
            self.numberOfNodesCreated = 1
            self.numberOfCitiesVisited = 0
            while stack:
                city = stack.pop()
                cityName = city.getName()
                if city.getParent():
                    self.allActionsTaken.append([cityName, city.getParent().getCity()])
                if cityName == self.goalCity:
                    self.numberOfCitiesVisited += 1
                    print('Visiting Goal', cityName)
                    pathToGoal = []
                    while city.getParent():
                        pathToGoal.append(city.getName())
                        city = city.getParent()
                    pathToGoal.append(city.getName())
                    pathToGoal.reverse()
                    self.searchSolution = pathToGoal
                    self.solutionFound = True
                    return self.searchSolution
                if cityName not in visited:
                    # print('Visiting ', city.getCity())
                    visited.append(cityName)
                    self.numberOfCitiesVisited += 1
                    cityNeighbours = city.getNeighbours()
                    for neighbour in cityNeighbours:
                        newNode = SearchTreeNode(neighbour, self.cityLocations[neighbour], city,
                                                 self.mappingCitiesToConnectedNeighbours[neighbour])
                        stack.append(newNode)
                        self.numberOfNodesCreated += 1

                else:
                    # already visited
                    continue
                # print('No solution Found.')
            return []


    def greedyBestFirstSearchManhattan(self):
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        stack = [startNode]
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        while stack:
            city = stack.pop()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
                print('Visiting Goal', cityName)
                pathToGoal = []
                while city.getParent():
                    pathToGoal.append(city.getName())
                    city = city.getParent()
                pathToGoal.append(city.getName())
                pathToGoal.reverse()
                self.searchSolution = pathToGoal
                self.solutionFound = True
                return self.searchSolution
            if cityName not in visited:
                # print('Visiting ', city.getCity())
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                mapCurrentNeighbourToHeuristic = {}
                for neighbour in cityNeighbours:
                    mapCurrentNeighbourToHeuristic[neighbour] = self.mapCitiesToDistanceToGoalManhattanDist[neighbour]

                while len(mapCurrentNeighbourToHeuristic) > 0:
                    addClosestToGoalNeighbour = max(mapCurrentNeighbourToHeuristic, key=mapCurrentNeighbourToHeuristic.get)
                    # print(addClosestToGoalNeighbour)
                    # print(self.mapCitiesToDistanceToGoalManhattanDist[addClosestToGoalNeighbour])
                    del mapCurrentNeighbourToHeuristic[addClosestToGoalNeighbour]
                    newNode = SearchTreeNode(addClosestToGoalNeighbour, self.cityLocations[addClosestToGoalNeighbour], city,
                                             self.mappingCitiesToConnectedNeighbours[addClosestToGoalNeighbour])
                    stack.append(newNode)
                    self.numberOfNodesCreated += 1

            else:
                # already visited
                continue
            # print('No solution Found.')
        return []


    def calcAllCityDistToGoalEuclidean(self):
        goalLocation = self.cityLocations[self.goalCity]
        for city in self.cities:
            currentCityLocation = self.cityLocations[city]
            x = (currentCityLocation[0] - goalLocation[0]) ** 2
            y = (currentCityLocation[1] - goalLocation[1]) ** 2
            z = x + y
            distance = math.sqrt(z)
            self.mapCitiesToDistanceToGoalEuclideanDist[city] = distance

    def calcAllCityDistanceToGoalManhattanDistance(self):
        goalLocation = self.cityLocations[self.goalCity]
        for city in self.cities:
            currentCityLocation = self.cityLocations[city]
            x = abs(currentCityLocation[0] - goalLocation[0])
            y = abs(currentCityLocation[1] - goalLocation[1])
            distance = x + y
            self.mapCitiesToDistanceToGoalManhattanDist[city] = distance