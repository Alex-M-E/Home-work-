#polynoms here
import matplotlib.pyplot as plt
import random as rd
import numpy as np

class poly:
    def __init__(self, coefs):
        self.coefs = coefs
 
    def simplify(self): #функция для обрезки нулей в старших степенях, образуются, например, при вычитании
        while self.coefs[-1] == 0 and len(self.coefs) > 1:
            self.coefs=self.coefs[: -1]
 
    def __add__(self, arg):
        res = poly(list(map(lambda x,y: x + y, self.coefs,arg.coefs)))
        res.coefs.extend(self.coefs[len(arg.coefs):] if len(self.coefs)>len(arg.coefs) else arg.coefs[len(self.coefs):])
 
        return res
 
    def __mul__(self, arg):
        if isinstance(arg, int) or isinstance(arg, float):
            return poly([arg*self.coefs[i] for i in range(len(self.coefs))])
 
        else:
            res = poly([0 for i in range(len(self.coefs)+len(arg.coefs) - 1)])
 
            for i in range(len(self.coefs)):
                for j in range(len(arg.coefs)):
                    res.coefs[i+j] += self.coefs[i]*arg.coefs[j]
            return res

    def __rmul__(self,arg): #чтоб можно было умножить число на многочлен (const*poly)
        if isinstance(arg, int) or isinstance(arg,float):
            return poly(list(map(lambda x:x*arg,self.coefs)))

 
    def __sub__(self, arg):
        return self + arg*(-1)
 
    def __floordiv__(self, arg):
        if len(self.coefs) < len(arg.coefs):
            return poly([0])#на занятии опечатался, надо вернуть нулевой многочлен
 
        else:
            res = poly([0 for i in range(len(self.coefs) - len(arg.coefs) + 1)])
            b = poly(self.coefs)
 
            for i in range(len(res.coefs) - 1, -1, -1):
                monom = poly([0 for j in range(i+1)])
                res.coefs[i] = b.coefs[-1]/arg.coefs[-1]
                monom.coefs[-1] = res.coefs[i]
                b = b - arg*monom
 
                b.coefs = b.coefs[:len(b.coefs) - 1]
 
            res.simplify()
            return res
 
    def __mod__(self, arg):
        if len(self.coefs) < len(arg.coefs):
            return poly(self.coefs)
 
        p = self//arg
        rem = self - arg*p
        rem.simplify()
 
        return rem
 
    def derivative(self):
        res = poly([self.coefs[i]*i for i in range(1, len(self.coefs))])
 
        if len(res.coefs) == 0:
            res.coefs.append(0)
        return res

    def FindValue(self, point):
        result = 0

        if len(self.coefs) == 0:
            return result 

        for i in range(len(self.coefs)):
            result += self.coefs[i]*(point**i)
        return result
 
    @staticmethod
    def GCD(a, b):
        p1 = poly(a.coefs)
        p2 = poly(b.coefs)
 
        while p1.coefs != [0] and p2.coefs != [0]:
            if len(p1.coefs) > len(p2.coefs):
                p1 = p1%p2
            else:
                p2 = p2%p1
 
        return p1+p2

def Newton(points, values):
    res = poly([values[0]]) #пустышка, в которую сложим результат
    p = poly([1]) #пустышка, в которую будем складывать многочлен (x-x0)(x-x1)..., чтобы его обновлять, а не считать заново каждый раз
    for i in range(1, len(values)):
        buf = poly([1]) #это коэффициент u_i, что стоит перед i-ым слагаемым в записи нашего многочлена
        p *= poly([-points[i-1], 1])

        buf *= values[i] - res.FindValue(points[i])

        for j in range(0, i):
            buf *= (1/(points[i] - points[j]))
        res += buf*p

    return res

# далле мой код
def Lagrang(x, y):
    res = poly([0])
    for i in range(len(x)):
        buf = poly([1])
        BUF = 1
        for j in range(len(x)):
            if i != j:
                buf *= poly([-x[j], 1])
                BUF *= (x[i] - x[j])
        buf *= (y[i] / BUF) 
        res += buf
    return res

x = np.linspace(-10, 10, 10)
y = [rd.uniform(-10, 10) for i in range(10)]

print(Lagrang(x, y).coefs)

lag = Lagrang(x, y)
points_l = np.linspace(-10, 10, 1000)
vals = [lag.FindValue(i) for i in points_l]
plt.scatter(x, y, c="red")
plt.plot(points_l, vals) #рисуем график многочлена
plt.show()

'''
points = np.linspace(-10, 10, 10) #10 точек равномерно размазаны по отрезку от -10 до

values = [rd.uniform(-10, 10) for i in range(10)] #10 случайных чисел от -10 до 10

p = Newton(points, values)

points_p = np.linspace(-10, 10, 1000) #точки, которые будут использоваться для построения графика многочлена
vals = [p.FindValue(i) for i in points_p] 
plt.scatter(points, values, c="red") #рисуем отдельные точки 
plt.plot(points_p, vals) #рисуем график многочлена
plt.show() #отображаем то, что ранее нарисовали
#plt.savefig("graph.png") костыль, который мне был необходим на занятии :)'''