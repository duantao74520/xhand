import numpy as np

def ApEn(U, m, r):

    def _maxdist(x_i, x_j):#求两个数组之间的最大距离
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):#求φm(r)
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]#（3）重构m维向量 m=2 那么range(i,i+2-1+1) 那么j=i,i+1 是一个x是一个m*(N-m+1)维的数组
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0) for x_i in x]#（4）求满足条件的个数 x_j从x[0]到x[N-m+1] 
        return (N - m + 1.0)**(-1) * sum(np.log(C)) #（5）将序列中所有的求和

    N = len(U)

    return abs(_phi(m+1) - _phi(m))#(6)求近似熵

# Usage example
#U = np.array([85, 80, 89] * 17)
# print(ApEn(U, 2, 3)) #m=2 r =3