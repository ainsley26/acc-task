# Notes on intro to ML

## ML Tutorial
> https://scikit-learn.org/stable/tutorial/basic/tutorial.html
Importing the demo datasets:
```python
from sklearn import datasets
iris = datsets.load_iris()
digits = datasets.load_digits()

print(digits.data)
print(digits.target)
```

The attribute `digits.data` is a 2D array of _n_ objects with _x_ features.
> i.e. `digits.data` = [obj1{f1, f2, f3, ...}, obj2{f1, f2, f3, ...}, ...]