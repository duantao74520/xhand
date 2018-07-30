import numpy as np


def envelop(U):
    U = np.fabs(U)
    U_mean = [np.mean(U[i*10:i*10+10]) for i in range(int(len(U)/10) - 1)]
    U_envelop = [np.mean(U_mean[i:i+10]) for i in range(len(U_mean) - 1)]
    return U_envelop


# U = np.array([1, 3, 3]*100)
# print(envelop(U))
