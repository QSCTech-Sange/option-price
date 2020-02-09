# option-price
<<<<<<< HEAD
`option-price` is a Python-based powerful but simple option price calculator. A GUI version is available [here](https://github.com/QSCTech-Sange/Options-Calculator).
=======
option-price is a Python-based powerful but simple option price calculator. A GUI version is available [here](https://github.com/QSCTech-Sange/Options-Calculator).
>>>>>>> master

# Installation
```shell
pip install option-price
```
# Usage
```python
from optionprice import Option
```

An option can be initialized by:
```
some_option = Option(european=False,
                    kind=1,
                    s0=100,
                    k=120,
                    t=45,
                    sigma=0.01,
                    r=0.05,
                    dv=0)
```

`option-price` has three approaches to calculate the price of the price of the option. They are
+ B-S-M
+ Monte Carlo
+ Binomial Tree

`option-price` will choose B-S-M algorithm by default. Prices can be simply calculated by

```python
some_option.getPrice()
```

Other methods of calculation are available by adding some parameters. For instance,
```python
some_option.getPrice(method='MC',iteration = 500000)
```

or

```python
some_option.getPrice(method='BT',iteration = 1000)
```

while MC stands for Monte Carlo and BT stands for Binomial Tree. 

The iteration has a default value 500. Note that the larger the value, the slower and more precise the price.