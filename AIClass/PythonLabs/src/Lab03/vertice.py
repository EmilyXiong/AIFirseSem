class Vertice:
    def __init__(self,key):
        self.__key = key
        self.__edges = []
        self.__groupId = 0
    
    def getKey(self):
        return self.__key
    
    def setKey(self, key):
        self.__key = key
    
    def getEdges(self):
        return self.__edges

    def add_edge(self, key,):
        self.__edges.append(key)
        
    def getGroupId(self):
        return self.__groupId
    
    def setGroupId(self, g_id):
        self.__groupId = g_id