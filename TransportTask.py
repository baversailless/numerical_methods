import numpy as np


def northWestCorner(supply, demand, costs):
    if sum(supply) == sum(demand):
        n = costs.shape[0]
        m = costs.shape[1]
        total = 0
        i = 0
        j = 0
        x = np.zeros((n, m))
        while i != n or j != m:
            k = 0
            if supply[i] < demand[j]:
                k = supply[i]
            else:
                k = demand[j]
            supply[i] -= k
            demand[j] -= k
            x[i][j] = k
            if supply[i] == 0 and i < n:
                i = i+1
            if demand[j] == 0 and j < m:
                j = j+1

        for i in range(n):
            for j in range(m):
                total += x[i][j]*costs[i][j]

    print("Total Cost = ", total)
    print('x: ')
    print(x)
    print(" ")
    print('c: ')
    print(costs)
    checkOptimality(x, costs, n, m)


def checkOptimality(x, costs, n, m):
    N = np.count_nonzero(x)
    check1 = (N == n + m - 1)
    if check1:
        u = np.array([np.nan] * n)
        v = np.array([np.nan] * m)
        l, p = np.where(x > 0)
        nz = list(zip(l, p))
        print(nz)
        u[0] = -1

        while any(np.isnan(u)) or any(np.isnan(v)):
            for i, j in nz:
                if np.isnan(u[i]) and not np.isnan(v[j]):
                    u[i] = costs[i, j] - v[j]
                elif not np.isnan(u[i]) and np.isnan(v[j]):
                    v[j] = costs[i, j] - u[i]
                else:
                    continue
        print(u)
        print(v)

    else:
        print('Degenerate Solution')


costs = np.array([[3, 4, 2, 1],
                  [1, 5, 4, 3],
                  [4, 1, 1, 2]])
supply = np.array([70, 60, 40])
demand = np.array([50, 30, 40, 50])
print('North West Corner method: ')
northWestCorner(supply, demand, costs)
