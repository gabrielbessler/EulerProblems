''' === Problem Statement ===

If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly three
    solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''


class Main(object):
    ''' Solution for Problem 39 '''

    def __init__(self):
        ''' DOCSTRING '''
        self.solutions = [[] for i in range(1001)]

    def find_triangles(self):

        # First, we know that a**2 + b**2 = c**2

        # Additionally, by the triangle inequality,
        # |a + b| <= |a| + |b|
        # Which implies that
        # |a + b| = |c| <= |a| + |b|
        # Which means that any triangle with length side c will have minimum
        # perimeter 2c.
        # This means that our solution must have c < 500
        for c in range(1, 500):
            solutionsFound = []
            for a in range(1, c):
                if a > c or a in solutionsFound:
                    continue
                b = (c**2 - a**2)**.5
                if b == int(b) and b > 0:
                    b = int(b)
                    solutionsFound.append(b)
                    if (a + b + c) <= 1000:
                        self.solutions[int(a + c + b)].append(
                            str(a) + \str(b) + str(c))

main = Main()
main.find_triangles()
# the length of each item in the list represents to the number of solutions
# for the perimeter corresponding with the index
print("The item with the most unique solutions has solutions: " +
      str(max(main.solutions, key=len)))
