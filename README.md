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
some_option = Option(european=True,
                    kind='call',
                    s0=100,
                    k=120,
                    t=45,
                    sigma=0.01,
                    r=0.05,
                    dv=0)
```
Or

```python
some_option = Option(european=False,
                    kind='put',
                    s0=100,
                    k=120,
                    sigma=0.01,
                    r=0.05,
                    start='2008-2-14'
                    end='2008-3-14'
                    dv=0)
```

You can check the option by 

```python
print(some_option)
```

which will print out the option’s info.

```python
Type:           European
Kind:           call
Price initial:  80
Price strike:   120
Volatility:     1.0%
Risk free rate: 5.0%
Start Date:     2020-03-24
Expire Date:    2020-04-24
Time span:      31.0 days
```

# Attributes

Name | Type |  Definition  
-|-|-
**european** | boolean | True if the option is an European option and False if it's an American one. 
**kind** | str | ‘call’ for call option while ‘put’ for put option. Other strs are not valid. 
**s0** | number | initial price 
**k** | int | strike price 
**sigma** | float | volatility of stock 
**r** | float | risk free interest rate per annum 
**[optional]dv** | float | dividend rate. 0 for non-stock option, which is also the default 
**[optional]t** | int | length of option in days 
**[optional]start** | str | beginning date of the option, string like '2008-02-14',default today 
**[optional]end** | str | end date of the option, string like '2008-02-14',default today plus param t 

Note that if start,end and t are all given, then t will choose the difference between end and start

Also, **either t or (start and end)** should exists

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

The iteration has a default value. Note that the larger the value, the slower and more precise the price.

Default value is a balance of speed and accuracy.