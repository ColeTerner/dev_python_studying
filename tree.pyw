        #ROOT class
class Tree:
    species="Oriented graph"
    def __init__(self,vertexes,edges):
        self.vertexes=vertexes
        self.edges=edges

    def description(self):
        return f"This graph contains {self.vertexes} vertexes and {self.edges} edges!"

    def grow(self):
        self.vertexes=self.vertexes+1
        self.edges=self.edges+1
        return f"The tree has grown to {self.vertexes} vertexes and {self.edges} edges..."

print(Tree.species)         #PROPERTY

        #Objects
or_graph_1= Tree(6,7)
or_graph_2= Tree(2,3)

print(or_graph_1.edges)     #7
print(or_graph_1.vertexes)  #6

print(or_graph_1.description()) #This graph contains 6 vertexes and 7 edges!
print(or_graph_1.grow())        #The tree has grown to 7 vertexes and 8 edges...


class Vertex:
    type="point"
    def __init__(self,number,color):
        self.number=number
        self.color=color

    def link_color(self):
        return f"My color is {self.color}!"
    def link_number(self):
        return f"My number is {self.number}!"
    

print(Vertex.type)      #point


