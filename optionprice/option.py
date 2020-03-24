import scipy.stats as sps
import numpy as np

class Option:

    """
    function: initialize an option
    :parm european: True if the option is an European option and False if it's an American one.
    :parm kind: 1 for call option while -1 for put option. Other number are not valid.
    :parm s0: initial price
    :parm k: strike price
    :parm t: length of option in days
    :parm sigma: volatility of stock
    :parm r: risk free interest rate per annu
    :parm dv: dividend rate. 0 for non-stock option, which is also the default
    :return Option
    """
    def __init__(self, european=False, kind=1, s0=100, k=80, t=60, r=0.05, sigma=0.01, dv=0):
        self.european = european
        self.kind = kind
        self.s0 = s0
        self.k = k
        self.t = t / 365
        self.sigma = sigma * 100
        self.r = r * 100
        self.dv = dv * 100
    
    """
    function: calculate the option price
    :parm method: indicate which method should be used to calculate.It can be one of "BSM","BT" and "MC".
    :parm iteration: the iteration times for "BT" and "MC"
    :return price
    """
    def getPrice(self,method="BSM",iteration = 5000):
        if method.upper() == "BSM" or method.upper() == "B-S-M":
            if self.european or self.kind == 1:
                d_1 = (np.log(self.s0 / self.k) + (
                        self.r - self.dv + .5 * self.sigma ** 2) * self.t) / self.sigma / np.sqrt(
                    self.t)
                d_2 = d_1 - self.sigma * np.sqrt(self.t)
                return self.kind * self.s0 * np.exp(-self.dv * self.t) * sps.norm.cdf(
                    self.kind * d_1) - self.kind * self.k * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d_2)


        elif method.upper() == "MC" or method.upper() == "Monte Carlo":
            if self.european or self.kind == 1:
                zt = np.random.normal(0, 1, iteration)
                st = self.s0 * np.exp((self.r - self.dv - .5 * self.sigma ** 2) * self.t + self.sigma * self.t ** .5 * zt)
                st = np.maximum(self.kind * (st - self.k), 0)
                return np.average(st) * np.exp(-self.r * self.t)


        elif method.upper() == "BT" or method.upper() == "Binomial Tree":
            delta = self.t / iteration
            u = np.exp(self.sigma * np.sqrt(delta))
            d = 1 / u
            p = (np.exp((self.r - self.dv) * delta) - d) / (u - d)
            
            tree = np.arange(0,iteration * 2 + 2,2,dtype=np.float128)
            tree[iteration//2 + 1:] = tree[:(iteration+1)//2][::-1]
            np.multiply(tree,-1,out=tree)
            np.add(tree,iteration,out=tree)
            np.power(u,tree[:iteration//2],out=tree[:iteration//2])
            np.power(d,tree[iteration//2:],out=tree[iteration//2:])
            np.maximum((self.s0 * tree - self.k) * self.kind,0,out=tree)

            for j in range(iteration):
                newtree = tree[:-1] * p + tree[1:] * (1 - p)
                newtree = newtree * np.exp(-self.r * delta)
                if not self.european:
                    compare = np.abs(iteration - j - 1 - np.arange(tree.size - 1) * 2).astype(np.float128)
                    np.power(u,compare[:len(compare)//2],out=compare[:len(compare)//2])
                    np.power(d,compare[len(compare)//2:],out=compare[len(compare)//2:])
                    np.multiply(self.s0,compare,out=compare)
                    np.subtract(compare,self.k,out=compare)
                    np.multiply(compare,self.kind,out=compare)
                    np.maximum(newtree, compare,out=newtree)
                tree = newtree

            return tree[0]


if __name__=='__main__':
    a = Option(european=False,
                    kind=1,
                    s0=100,
                    k=120,
                    t=45,
                    sigma=0.01,
                    r=0.05,
                    dv=0)
    
    print(a.getPrice())
    print(a.getPrice(method='MC',iteration = 500000))
    print(a.getPrice(method='BT',iteration = 1000))
