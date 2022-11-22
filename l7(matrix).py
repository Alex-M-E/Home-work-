# грамостко но работает.

class matrix():
    def __init__(self, d):
        self.coords = d
        self.height = len(d)
        self.width = len(d[0])
    def __add__(self, self1):
        if isinstance(self1, matrix) and isinstance(self, matrix):
            if self.height == self1.height and self.width == self1.width:
                c = [[0 for _ in range(self1.width)] for _ in range(self1.height)]
                for i in range(self1.height):
                    for j in range(self1.width):
                        c[i][j] = self.coords[i][j] + self1.coords[i][j]
                return matrix(c)
            return None
        return None
    def __str__(self):
        return str(self.coords)
    def __mul__(self, self1):
        if self is None or self1 is None:
            return None
        if isinstance(self1, matrix) and isinstance(self, matrix):
            if self.width == self1.height:
                c = [[self.coords[y][x] for x in range(self1.width)] for y in range(self.height)]
                w = 0
                for i in range(self.height):
                    for o in range(self1.width):
                        w = 0
                        for j in range(self1.height):
                            w = w + (self1.coords[j][o] * self.coords[i][j])
                        c[i][o] = w
                return matrix(c)
            else:
                if self1.width == self.height:
                    c = [[self.coords[y][x] for x in range(self.width)] for y in range(self1.height)]
                    for i in range(self1.height):
                        for o in range(self.width):
                            w = 0
                            for j in range(self.height):
                                w = w + (self.coords[j][o] * self1.coords[i][j])
                            c[i][o] = w
                    return matrix(c)
                else:
                    return None

        else:
            if isinstance(self1, float) or isinstance(self1, int):
                c = [[self.coords[y][x] for x in range(self.width)] for y in range(self.height)]
                for i in range(len(c)):
                    for j in range(len(c[0])):
                        c[i][j] = c[i][j] * self1
                return matrix(c)
            return None
        return None
    def __rmul__(self, self1):
        if self is None or self1 is None:
            return None
        if isinstance(self1, matrix) and isinstance(self, matrix):
            return None
        else:
            if isinstance(self1, float) or isinstance(self1, int):
                c = [[self.coords[y][x] for x in range(self.width)] for y in range(self.height)]
                for i in range(len(c)):
                    for j in range(len(c[0])):
                        c[i][j] = c[i][j] * self1
                return matrix(c)
            return None
        return None
        
        
        
m1 = matrix([[3, -1, 2], [4, 2, 0], [-5, 6, 1]])
m2 = matrix([[8, 1], [7, 2], [2, -3]])
m3 = m2 * m1
print(m3)
m4 = m3 * 3
print(m4)
m5 = m1 + m2
print(m5) # Выведет None (Собствено так и нужно)
m6 = m3 + m4
print(m6)