from point import Point

class Cluster:
    def __init__(self):
        self.points = [] 
        self.centroid = [] 

    def add_point(self, point:Point):
        self.points.append(point)

    def new_centroid(self):
        dimensions = self.points[0].dimensions
        new_centroid = [0.0] * dimensions

        for d in range(dimensions):
            for p in self.points:
                new_centroid[d] += p.coordinates[d]

        for d in range(dimensions):
            new_centroid[d] /= len(self.points)
        
        self.centroid = Point(new_centroid)
