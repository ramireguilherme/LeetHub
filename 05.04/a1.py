from math import sin, cos, tan, exp
def brent_method(f, a, b, tol=1.0e-6, max_iter=100000):
    # find fa and fb with different signs
    if f(a) * f(b) > 0:
        found_pair = False
        while f(a) * f(b) > 0 and (0 <= a <= 1) and (0 <= b <= 1):
            a += 0.007
            b -= 0.005
            if f(a) * f(b) < 0:
                found_pair = True
                break
        if not found_pair:
            raise ValueError("No root found in the interval [0, 1]")

    fa = f(a)
    fb = f(b)
    
    if abs(fa) < abs(fb):
        a, b = b, a
        fa, fb = fb, fa
    
    c = a
    fc = fa
    d = e = b - a
    
    for __ in range(max_iter):
        if fb * fc > 0:
            c = a
            fc = fa
            d = e = b - a
        
        if abs(fc) < abs(fb):
            a, b = b, c
            c = a
            fa, fb, fc = fb, fc, fa
        
        tol1 = 2.0 * tol * abs(b) + 0.5 * tol
        xm = 0.5 * (c - b)
        
        if abs(xm) <= tol1 or fb == 0.0:
            return b
        
        if abs(e) >= tol1 and abs(fa) > abs(fb):
            s = fb / fa
            if a == c:
                p = 2.0 * xm * s
                q = 1.0 - s
            else:
                q = fa / fc
                r = fb / fc
                p = s * (2.0 * xm * q * (q - r) - (b - a) * (r - 1.0))
                q = (q - 1.0) * (r - 1.0) * (s - 1.0)
            
            if p > 0:
                q = -q
            p = abs(p)
            
            min1 = 3.0 * xm * q - abs(tol1 * q)
            min2 = abs(e * q)
            if 2.0 * p < min(min1, min2):
                e = d
                d = p / q
            else:
                d = xm
                e = d
        else:
            d = xm
            e = d
        
        a = b
        fa = fb
        if abs(d) > tol1:
            b += d
        else:
            b += tol1 if xm >= 0 else -tol1
        fb = f(b)
    
    raise RuntimeError("Maximum number of iterations exceeded")
a = 0
b = 1

while True:
    try :
        p,q,r,s,t,u = map(int, input().split())
        f = lambda x: p*exp(-x) + q*sin(x) + r*cos(x) + s*tan(x) + t*x*x + u
        root = brent_method(f, a, b)
        print("{:.4f}".format(root))
    except EOFError:
        break
    except ValueError:
        print("No solution")