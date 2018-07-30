import numpy as np 
import matplotlib.pyplot as plt
import ApEn
import SampEn
import mean
import TKE
import envelope

N = 64  # 滑动窗大小
r = 0.2
#
arr = np.loadtxt("E:\\嵌入式肌电手\\肌电数据\\谢志亮emg数据\\emg_data.txt")
arr_CB = arr[:, 2]

# arr_CB = arr_CB - np.mean(arr_CB)  # 去中心化


def emgApEn(arr, m, r):
    std_all = np.std(arr)
    arr_fram = [[arr[i*N+j] for j in range(N)] for i in range(int(len(arr)/N))]
    # std_single = np.std(arr_fram,axis=0)
    arr_ApEn = [ApEn.ApEn(x, m, r*std_all) for x in arr_fram]
    return arr_ApEn


def emgSampEn(arr, m, r):
    std_all = np.std(arr)
    arr_fram = [[arr[i*N+j] for j in range(N)] for i in range(int(len(arr)/N))]
    arr_SampEn = [SampEn.SampEn(x, m, r*std_all) for x in arr_fram]
    return arr_SampEn


def emgSlidMean(arr):
    arr_fram = [[arr[i*N+j] for j in range(N)] for i in range(int(len(arr)/N))]
    arr_slideMean = [mean.slidMean(x) for x in arr_fram]   
    return arr_slideMean


def emgTke(U):
    arr_TKE = TKE.tke(U)
    return arr_TKE


def emgEnvelop(U):
    arr_envelop = envelope.envelop(U)
    return arr_envelop


plt.figure('原始数据')
plt.title('source')
plt.plot(arr_CB)
plt.savefig("source.jpg")

plt.figure("傅里叶")
plt.plot(np.fft.fft(arr_CB))

plt.figure("ApEn")
plt.title('ApEn r=0.2')
plt.plot(emgApEn(arr_CB, 2, r))
plt.savefig("ApEn.jpg")

plt.figure("SampEn")
plt.title("SampEn r=0.2")
plt.plot(emgSampEn(arr_CB, 2, r))
plt.savefig("SampEn.jpg")

plt.figure("slideMean")
plt.title("slideMean")
plt.plot(emgSlidMean(arr_CB))
plt.savefig("slideMean.jpg")


plt.figure("TKE")
plt.title("TKE")
plt.plot(emgTke(arr_CB))
plt.savefig("TKE.jpg")

plt.figure("envelop")
plt.title("envelop")
plt.plot(emgEnvelop(arr_CB))
plt.savefig("envelop.jpg")

plt.show()