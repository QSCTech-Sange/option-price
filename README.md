# option-price
`option-price` is a Python-based powerful but simple option price calculator. It makes use of vectorization, which makes it pretty fast.

A GUI version is available [here](https://github.com/QSCTech-Sange/Options-Calculator). 

Docs are available [here](https://qsctech-sange.github.io/option-price). 

# Installation
```shell
pip install option-price
```
# Quick Start
```python
from optionprice import Option
```

An option can be initialized by:
```python
some_option = Option(european=False,
                    kind=1,
                    s0=100,
                    k=120,
                    t=45,
                    sigma=0.01,
                    r=0.05,
                    dv=0)
```
# Attributes
Name | Type |  Definition  
-|-|-
**european** | boolean | True if the option is an European option and False if it's an American one. |
**kind** | int | 1 for call option while -1 for put option. Other number are not valid. |
**s0** | number | initial price |
**k** | int | strike price |
**t** | int | length of option in days |
**sigma** | float | volatility of stock |
**r** | float | risk free interest rate per annum |
**dv** | float | dividend rate. 0 for non-stock option, which is also the default |

# Calculate
`option-price` has three approaches to calculate the price of the price of the option. They are
+ B-S-M
+ Monte Carlo
+ Binomial Tree

`option-price` will choose B-S-M algorithm by default. Prices can be simply calculated by

```python
price = some_option.getPrice()
```

Other methods of calculation are available by adding some parameters. For instance,
```python
price = some_option.getPrice(method='MC',iteration = 500000)
```

or

```python
price = some_option.getPrice(method='BT',iteration = 1000)
```

while MC stands for Monte Carlo and BT stands for Binomial Tree. 

The iteration has a default value 5000. Note that the larger the value, the slower and more precise the price.