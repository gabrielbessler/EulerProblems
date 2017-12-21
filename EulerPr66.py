'''  === Problem Statement ===

Consider quadratic Diophantine equations of the form:
x2 – Dy2 = 1
For example, when D=13, the minimal solution in x is
6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers
when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
we obtain the following:
3**2 – 2×2**2 = 1 (3, 2) D = 2
2**2 – 3×1**2 = 1 (2, 1) D = 3
9**2 – 5×4**2 = 1 (9, 4) D = 5
5**2 – 6×2**2 = 1 (5, 2) D = 6
8**2 – 7×3**2 = 1 (8, 3) D = 7
Hence, by considering minimal solutions in x for D ≤ 7,
    the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for
    which the largest value of x is obtained.
'''


def problem66(self):

        list_1 = set([x**2 for x in range(1, 32)])
        list_2 = set([x for x in range(1, 1000)])
        list_2 = list_2 - list_1
        '-'
        currMax, currMaxVal = 0, 0
        for i, D in enumerate(list_2):
            if D == 61 or D == 97:
                continue
            eqn = lambda x, y: x**2 - (D * (y**2))
            x = 1
            y = 1
            while eqn(x, y) != 1:
                if x % 100000 == 0:
                    print(x, y, eqn(x, y))
                if eqn(x, y) > 1:
                    y += 1
                else:
                    x += 1
            print("For D = " + str(D) + ", obtained minimum solution: " +
                  str(x) + "," + str(y))
            if x > currMaxVal:
                currMaxVal = x
                currMax = D
        return 0