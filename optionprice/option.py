import scipy.stats as sps
import numpy as np

class Option:

    # european 为 欧式期权 (True 为欧式期权)
    # kind 看涨或看跌（Put 为 -1 , Call 为 1）
    # s0 标的资产现价
    # k 期权执行价
    # t 期权到期时间 - 现在时间,以天计
    # r 适用的无风险利率，连续复利
    # sigma 适用的波动率，
    # dv 股利信息，连续复利
    def __init__(self, european=False, kind=1, s0=100, k=80, t=60, r=0.05, sigma=0.01, dv=0):
        self.european = european
        self.kind = kind
        self.s0 = s0
        self.k = k
        self.t = t /365
        self.sigma = sigma
        self.r = r
        self.dv = dv
        self.bsprice = "Uncounted"
        self.mcprice = "Uncounted"
        self.btprice = "Uncounted"
        self.price = {'B-S-M':'Uncounted','Monte Carlo':'Uncounted','Binary Tree':'Uncounted'}

    def getPrice(self,method="BSM",iteration = 500):
        if method.upper() == "BSM" or method.upper() == "B-S-M":
            if self.european or self.kind == 1:
                d_1 = (np.log(self.s0 / self.k) + (
                        self.r - self.dv + .5 * self.sigma ** 2) * self.t) / self.sigma / np.sqrt(
                    self.t)
                d_2 = d_1 - self.sigma * np.sqrt(self.t)
                self.price['B-S-M'] = self.kind * self.s0 * np.exp(-self.dv * self.t) * sps.norm.cdf(
                    self.kind * d_1) - self.kind * self.k * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d_2)
            else:
                self.price['B-S-M'] = "Please use binary tree to calculate American call option."
            print(self.price['B-S-M'])

        elif method.upper() == "MC" or method.upper() == "Monte Carlo":
            if self.european or self.kind == 1:
                zt = np.random.normal(0, 1, iteration)
                st = self.s0 * np.exp((self.r - self.dv - .5 * self.sigma ** 2) * self.t + self.sigma * self.t ** .5 * zt)
                st = np.maximum(self.kind * (st - self.k), 0)
                self.price['Monte Carlo'] = np.average(st) * np.exp(-self.r * self.t)
            else:
                self.price['Monte Carlo'] = "Please use binary tree to calculate American call option."
            print(self.price['Monte Carlo'])

        elif method.upper() == "BT" or method.upper() == "Binary Tree":
            if iteration % 2 != 0:
                iteration += 1
            delta = self.t / iteration
            u = np.exp(self.sigma * np.sqrt(delta))
            d = 1 / u
            p = (np.exp((self.r - self.dv) * delta) - d) / (u - d)
            tree = []
            for j in range(int(iteration / 2) + 1):
                i = j * 2
                temp = self.s0 * np.power(u, iteration - i)
                temp = np.max([(temp - self.k) * self.kind, 0])
                tree.append(temp)
            for j in range(1, int(iteration / 2) + 1):
                i = j * 2
                temp = self.s0 * np.power(d, i)
                temp = np.max([(temp - self.k) * self.kind, 0])
                tree.append(temp)
            for j in range(0, iteration):
                newtree = []
                for i in (range(len(tree) - 1)):
                    temp = tree[i] * p + (1 - p) * tree[i + 1]
                    temp = temp * np.exp(-self.r * delta)
                    if not self.european:
                        # 每一层的最高幂次
                        k = iteration - j - 1
                        if i < (k + 1) / 2:
                            power = k - i * 2
                            compare = self.s0 * np.power(u, power)
                        else:
                            power = i * 2 - k
                            compare = self.s0 * np.power(d, power)
                        temp = np.max([temp, (compare - self.k) * self.kind])
                    newtree.append(temp)
                tree = newtree
            self.price['Binary Tree'] = tree[0]
            print(self.price['Binary Tree'])   
       
        else:
            print("Supported method parameters are BSM, MC, BT")