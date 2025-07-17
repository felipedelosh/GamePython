"""
FelipedelosH
This is a state machine
a pointer mouve node to node 

"""

class StateMachine:
    def __init__(self) -> None:
        self.pointer = None # Say what node stay currently
        self.node = []
        self.edges = {}

    def addNode(self, x):
        if x not in self.node:
            self.node.append(x)
            # For default the sm init in initial point
            if self.pointer == None:
                self.pointer = x

    def addConection(self, a, b, key):
        """
        a = origin node
        b = next node
        key = key to jump
        """
        if a in self.node and b in self.node:
            if a in self.edges.keys():
                conection = self.edges[a]
                conection.append((b, key))
            else:
                conection = [(b, key)]
                self.edges[a] = conection

    def setInitialPointer(self, node):
        """
        The machine needs initial point to move
        """
        if node in self.node:
            self.pointer = node


    def insertSimbol(self, key):
        """
        key is a simbol to insert in machine
        move a pointer
        """
        if self.pointer != None:
            for i in self.edges[self.pointer]:
                if key == i[1]:
                    self.pointer = i[0]

    def mouvePointer(self, symbol):
        """
        Enter a symbol and the poiter mouve
        """
        for i in self.edges[self.pointer]:
            if symbol == i[1]:
                #print("Me he movido a", i[0])
                # Mouve a pivot
                self.pointer = i[0]
                break

    def viewMachine(self):
        print("====================")
        print("The machine is:")
        print(self.edges)
        print("The pivot is")
        print(self.pointer)
