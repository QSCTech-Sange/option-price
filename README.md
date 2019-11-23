# option-price
option-price is a Python-based powerful but simple option price calculator.

# Installation
```shell
pip install option-price
```
# Usage
```python
from optionprice import Option
```

You can initialize an option through this:
```
some_option = Option(european=False,
                    kind = 1,
                    s0 = 100,
                    k=120,
                    t=45,
                    sigma=0.01,
                    r=0.05
                    dv = 0)
```

`option-price` has three approaches to calculate the price of the price of the option. They are
+ B-S-M
+ Monte Carlo
+ Binary Tree

`option-price` will pick B-S-M by default. You can simply get the price by using
```python
some_option.getPrice()
```

If you want to calculate in other ways, you can use
```python
some_option.getPrice(method='MC',iteration = 500000)
```

or

```python
some_option.getPrice(method='BT',iteration = 1000)
```

while MC stands for Monte Carlo and BT stands for Binary Tree.