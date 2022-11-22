from math import sqrt

class vector():
    def __init__(self, *args):
        self.coords = list(args)
        self.dim = len(args)

    def __add__(self, other):
        if isinstance(other, vector) and other.dim == self.dim:
            return vector(*list(map(lambda x,y: x+y, self.coords, other.coords)))
    def __sub__(self, other):
        if isinstance(other, vector) and other.dim == self.dim:
            return vector(*list(map(lambda x,y: x-y, self.coords, other.coords)))

    def __mul__(self, other):
        if isinstance(other, vector) and other.dim == self.dim:
            return sum(list(map(lambda x,y:x*y, self.coords, other.coords)))

        else:
            return vector(*list(map(lambda x: x*other, self.coords)))

    def __rmul__(self, other):
        if isinstance(other, vector) and other.dim == self.dim:
            return sum(list(map(lambda x,y:x*y, self.coords, other.coords)))

        else:
            return vector(*list(map(lambda x: x*other, self.coords)))

    def length(self):
        return sqrt(self*self)

    @staticmethod
    def cos_angle(v1, v2):
        return (v1*v2)/( (v1.length())*(v2.length()))

    def __str__(self):
        return str(self.coords)
    @staticmethod
    def isparal(self, other):
        if isinstance(other, vector) and other.dim == self.dim:
            d = set()
            for i in range(len(self.coords)):
                if self.coords[i] == 0:
                    if other.coords[i] != 0:
                        return False
                else:
                    if other.coords[i] == 0:
                        return False
                    d.add(other.coords[i] / self.coords[i])
            if len(d) == 1:
                return True
            return False
        return None
                    
        

v1 = vector(1, 0)
v2 = vector(0, 1)

v3 = v1 * 2
v4 = 2 * v2
v5 = v3 - v4
v6 = v1 * v2
print(v1)
print(v6)
print(v3)
print(v4)
print(vector.isparal(v1, v2))
print(vector.isparal(vector(1, 0), vector(2, 0)))
print(vector.cos_angle(v1, v2))


