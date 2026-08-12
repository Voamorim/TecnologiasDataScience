class Point:
    def __init__(self, coordinates:list):
        self.coordinates = coordinates 
        self.dimensions = len(coordinates)

    def print(self):
        print('(', end='')
        for i in range(self.dimensions):
            if i != self.dimensions - 1:
                print(self.coordinates[i], end=',')
            else:   
                print(self.coordinates[i], end=')')
        print()

    def euclidean_distance(self, other):
        distance = 0.0

        for i in range(self.dimensions):
            distance += (self.coordinates[i] - other.coordinates[i]) ** 2

        distance = distance ** 0.5
        return distance
    
