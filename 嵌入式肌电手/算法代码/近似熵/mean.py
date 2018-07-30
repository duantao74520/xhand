'''
滑动平均值算法
'''
import numpy as np 


def slidMean(U):
    abs_U = np.fabs(U)
    return np.mean(abs_U)


# sample
# U = [1, -1, -1]
# print(slidMean(U))