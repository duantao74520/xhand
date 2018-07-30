import numpy as np


def SampEn(U, m, r):
    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        B = [(len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) - 1.0) / (N - m) for x_i in x]#因为有本身 直接减一就好了
        for i in range(len(B)):
            if B[i] == 0:
                B[i] = 0.00001
        return (N - m + 1.0)**(-1) * sum(B)

    N = len(U)

    return -np.log(_phi(m+1) / _phi(m))

# Usage example
# U = np.array([85, 80, 89] *17)
# print(SampEn(U,2,3))