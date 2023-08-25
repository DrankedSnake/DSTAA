class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.edges = []

    def push(self, edge: Edge):
        self.edges.append(edge)
