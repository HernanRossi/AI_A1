import math
from SearchTreeNode import SearchTreeNode
import queue

class stateTuple(object):
    def __init__(self, priority, state):
        self.priority = priority
        self.state = state
        return
    def __eq__(self, other):
        return not self.priority < other.priority and not other.priority < self.priority
    def __lt__(self, other):
        return self.priority < other.priority
    def __gt__(self, other):
        return  other.priority < self.priority

class AStar:

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
        self.maxNumberOfNodesInMemory = 0

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


    def AStarEuclidean(self):
        nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        priorityQueue = queue.PriorityQueue()
        priorityQueue.put((0.0, startNode))
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        self.maxNumberOfNodesInMemory = 0

        while not priorityQueue.empty():
            priority, city = priorityQueue.get()
            if self.maxNumberOfNodesInMemory < priorityQueue.qsize():
                self.maxNumberOfNodesInMemory = priorityQueue.qsize()
            cityName = city.getName()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
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
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                costFromStart = 0
                for neighbour in cityNeighbours:
                    if not nodeAlreadyCreated[neighbour]:
                        if neighbour not in visited:
                            costUpToParent = city.pathCost
                            costFromParent = self.calcCostFromParent(city.getCity(), neighbour)
                            costFromStart = costUpToParent + costFromParent
                            costToGoal = self.mapCitiesToDistanceToGoalEuclideanDist[neighbour]
                            newNode = SearchTreeNode(neighbour,
                                                     self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            nodeAlreadyCreated[neighbour] = True
                            newNode.pathCost = costFromStart
                            self.numberOfNodesCreated += 1
                            heuristicCost = costFromStart + costToGoal
                            priorityQueue.put((heuristicCost, newNode))
        return []

    def AStarNoHeuristic(self):
        nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        priorityQueue = queue.PriorityQueue()
        tup = stateTuple(0.0, startNode)
        priorityQueue.put(tup)
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        self.maxNumberOfNodesInMemory = 0

        while not priorityQueue.empty():
            cityTuple =priorityQueue.get()
            city = cityTuple.state
            cityName = city.getName()
            if self.maxNumberOfNodesInMemory < priorityQueue.qsize():
                self.maxNumberOfNodesInMemory = priorityQueue.qsize()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
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
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                mapCurrentNeighbourToHeuristic = {}
                costFromStart = 0
                for neighbour in cityNeighbours:
                    if not nodeAlreadyCreated[neighbour]:
                        if neighbour not in visited:
                            costUpToParent = city.pathCost
                            costFromParent = self.calcCostFromParent(city.getCity(), neighbour)
                            costFromStart = costUpToParent + costFromParent
                            costToGoal = 0.00

                            newNode = SearchTreeNode(neighbour,
                                                     self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            nodeAlreadyCreated[neighbour] = True
                            newNode.pathCost = costFromStart
                            self.numberOfNodesCreated += 1
                            heuristicCost = costFromStart * 1.0
                            tup = stateTuple(heuristicCost, newNode)
                            priorityQueue.put(tup)
        return []

    def AStarManhattan(self):
        nodeAlreadyCreated = {
            'A': False, 'B': False, 'C': False, 'D': False, 'E': False, 'F': False,
            'G': False, 'H': False, 'I': False, 'J': False, 'K': False, 'L': False,
            'M': False, 'N': False, 'O': False, 'P': False, 'Q': False, 'R': False,
            'S': False, 'T': False, 'U': False, 'V': False, 'W': False, 'X': False,
            'Y': False, 'Z': False
        }
        self.allActionsTaken = []
        self.searchSolution = []
        self.solutionFound = False
        visited = []
        startNode = SearchTreeNode(self.startCity, self.cityLocations[self.startCity], False,
                                   self.mappingCitiesToConnectedNeighbours[self.startCity])
        priorityQueue = queue.PriorityQueue()
        priorityQueue.put((0.0,startNode))
        self.numberOfNodesCreated = 1
        self.numberOfCitiesVisited = 0
        self.maxNumberOfNodesInMemory = 0

        while not priorityQueue.empty():
            priority, city = priorityQueue.get()
            cityName = city.getName()
            if self.maxNumberOfNodesInMemory < priorityQueue.qsize():
                self.maxNumberOfNodesInMemory = priorityQueue.qsize()
            if city.getParent():
                self.allActionsTaken.append([cityName, city.getParent().getCity()])
            if cityName == self.goalCity:
                self.numberOfCitiesVisited += 1
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
                visited.append(cityName)
                self.numberOfCitiesVisited += 1
                cityNeighbours = city.getNeighbours()
                mapCurrentNeighbourToHeuristic = {}
                costFromStart = 0
                for neighbour in cityNeighbours:
                    if not nodeAlreadyCreated[neighbour]:
                         if neighbour not in visited:
                            costUpToParent = city.pathCost
                            costFromParent = self.calcCostFromParent(city.getCity(), neighbour)
                            costFromStart = costUpToParent + costFromParent
                            costToGoal = self.mapCitiesToDistanceToGoalManhattanDist[neighbour]
                            newNode = SearchTreeNode(neighbour,
                                                     self.cityLocations[neighbour], city,
                                                     self.mappingCitiesToConnectedNeighbours[neighbour])
                            nodeAlreadyCreated[neighbour] = True
                            newNode.pathCost = costFromStart
                            self.numberOfNodesCreated += 1
                            heuristicCost = costFromStart + costToGoal
                            priorityQueue.put((heuristicCost, newNode) )
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

    def calcCostFromParent(self, fromCity, currentCity):
        startLocation = self.cityLocations[fromCity]
        currentCityLocation = self.cityLocations[currentCity]
        x = (startLocation[0] - currentCityLocation[0]) ** 2
        y = (startLocation[1] - currentCityLocation[1]) ** 2
        z = x + y
        distance = math.sqrt(z)
        return distance

    def calcAllCityDistanceToGoalManhattanDistance(self):
        goalLocation = self.cityLocations[self.goalCity]
        for city in self.cities:
            currentCityLocation = self.cityLocations[city]
            x = abs(currentCityLocation[0] - goalLocation[0])
            y = abs(currentCityLocation[1] - goalLocation[1])
            distance = x + y
            self.mapCitiesToDistanceToGoalManhattanDist[city] = distance