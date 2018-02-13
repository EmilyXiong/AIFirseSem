class nodeEdge:
    def __init__(self, fromNodeName, toNodeName, distance):
        self.__from = fromNodeName
        self.__to = toNodeName
        self.__distance = distance
        self.__visited = False
        
    def getFromNodeName(self):
        return self.__from
    def getToNodeName(self):
        return self.__to
    def getDistance(self):
        return self.__distance
    def hasVisited(self):
        return self.__visited
    def setVisited(self, value):
        self.__visited = value
