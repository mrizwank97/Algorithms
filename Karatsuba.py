import math
def Karatsuba(x, y):
    if(x < 10 or y < 10):
        return x * y
    else:
        n = max(len(str(x)),len(str(y)))
        m = math.ceil(n/2)
        a = int(x/pow(10, m))
        b = x % pow(10, m)
        c = int(y/pow(10,m))
        d = y % pow(10,m)
        z1 = Karatsuba(a,c)
        z2 = Karatsuba(b,d)
        z3 = Karatsuba(a+b,c+d)

        return pow(10,2*m) * z1 + pow(10,m) * (z3-z2-z1) + z2


print(Karatsuba(1234,5678))
