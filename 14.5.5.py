def diskriminant(a, b, c):
    return b**2 - 4*a*c


def quadratic_solve(a, b, c):
    if diskriminant(a, b, c) < 0:
        return "Нет вещественных корней"
    elif diskriminant(a, b, c) == 0:
        return -b/(2*a)
    else:
        return (-b-diskriminant(a, b, c)**0.5)/(2*a), (-b+diskriminant(a, b, c)**0.5)/(2*a)


L = list(map(float, input().split()))

M = {'a': 1,
     'b': 0,
     'c': -1}
print(quadratic_solve(*L))
print(quadratic_solve(**M))
