import numpy as np 


def tke(U):
    U = U-np.mean(U)  # 求均值
    print(U)
    x = [(U[i]**2-U[i+1]*U[i-1]) for i in range(1, len(U)-1)]
    return x


# U = np.array([1, 3, 3]*10)
# print(tke(U))
