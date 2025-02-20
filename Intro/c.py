from functools import reduce
correspondes = {
    1:7,
    2:2,
    3:3,
    4:3,
    5:4,
    6:2,
    7:5,
    8:1,
    9:2,
    0:2
}
a = [correspondes[int(d)] for d in str(input())]
print(a[0]*a[1])