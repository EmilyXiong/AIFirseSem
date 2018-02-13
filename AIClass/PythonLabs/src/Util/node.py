class Node:
    def __init__(self,key,parent=None):
        self.__key = key
        self.__children = []
        self.__parentKey=parent
    
    def key(self):
        return self.__key
    
    def setKey(self, key):
        self.__key = key
    
    def children(self):
        return self.__children
    
    def parentKey(self):
        return self.__parentKey
    
    def setParentKey(self, parent):
        self.__parentKey = parent

    def add_child(self, key,):
        self.__children.append(key)