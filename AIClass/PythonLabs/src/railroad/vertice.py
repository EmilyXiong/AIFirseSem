class vertice:
    def __init__(self,name, x, y):
        self.__name = name
        self.__fullName = ''
        self.__x = x
        self.__y = y
        self.__edges=[]
    
    def getName(self):
        return self.__name
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getFullName(self):
        return self.__fullName
    def setFullName(self, fullName):
        self.__fullName = fullName
    def addEdge(self, name):
        self.__edges.append(name)
    def getEdges(self):
        return self.__edges