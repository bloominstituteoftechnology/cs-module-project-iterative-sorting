# my implementation of the kd_tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.median_point = None
        self.dimension = None # This will tell the dimension that the 
                              # cut is found at


class KD_tree:
    def __init__(self, data, depth):
        self.head = Node(data)
        self.depth = depth
        self.__dimen = []
        self.__build(data)
    

    def __build(self, data):
        # will first check the dimensionsf
        # doing the sorting of dimensions
        # finding the length of the data
        
        self.__sort_dim(data)
        # building the tree
        self.__build_tree(data, self.depth, Node(data))



    def __sort_dim(self, data):
        theLen = len(data[0])
        # looping through the different dimensions
        for i in range(theLen):
            self.__dimen.append(data[:, i])


    def __build_tree(self, data, curDepth, theNode):
        # This will be the recursive function that will 
        # build the tree
        # building will occur until there are 20 point or the 
        # depth is reached
        if len(theNode.data) > 


