from node import Node

class Tree:
    
    def __init__(self):
        self.__root = None
        self.__nodes = {}
        self.__nodesAtnthLevel = []
    
    def nodes(self):
        return self.__nodes
    
    def setNodes(self, newNodes):
        self.__nodes = newNodes
        
    def add_firstnode(self, key):
        node = Node(key, None)
        self.__nodes[key] = node
        self.__root = key
        
    def add_node(self, key, parent):
        node = Node(key)
        node.setParentKey(parent)
        self.__nodes[key]=node
        self.__nodes[parent].add_child(key)
        
    def traverse(self, key):
        queue = [key]
        while queue:
            yield queue[0]
            expansion = self.__nodes[queue[0]].children()
            queue = queue[1:] + expansion
    
    def depthTraverse(self, key):
        queue = [key]
        while queue:
            yield queue[0]
            expansion = self.__nodes[queue[0]].children()
            queue = expansion + queue[1:]
            
    def maxSteps(self, startKey):
        return self.maxDepth(self.nodes().get(startKey))
    
    def maxDepth(self, node):
        if not node.children():
            return 0
        else:
            depth_of_children=[]
            for child in node.children():
                depth_of_children.append(self.maxDepth(self.nodes().get(child)))
            return max(depth_of_children)+1
          
    def nodesAtnthLevel(self, n):
        self.__nodesAtnthLevel = []
        if self.__root != None:
            self.getNodesAtNthLevel(self.nodes().get(self.__root), n)
        return self.__nodesAtnthLevel
    
    def getNodesAtNthLevel(self, startNode, n):
        if n == 0:
            self.__nodesAtnthLevel.append(startNode.key())
            return
        if not startNode.children():
            return
        else:
            for child in startNode.children():
                self.getNodesAtNthLevel(self.nodes().get(child), n-1)
                
        
    