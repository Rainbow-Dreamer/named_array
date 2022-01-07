# named_array

This is a python module that extends numpy array to be able to have column names to index with.

## Installation

```
pip install named_array
```

Note that you need to have numpy installed already to use this module.

## Usage

```python
import numpy as np
from named_array import named_array

# the keyword arguments for named_array are exactly the same with numpy array,
# but with an extra keyword `colnames`, which is a list of the column names for each column
A = named_array([[1,2,3],[4,5,6]], colnames=['a', 'b', 'c'])

>>> A
named_array([[1, 2, 3],
             [4, 5, 6]])

# you can index a column by name
>>> A['a']
named_array([1, 4])

# you can extract several columns as a new array
# by a tuple or a list of column names
>>> A['a', 'b']
array([[1, 2],
       [4, 5]])

>>> A[['a', 'b']]
array([[1, 2],
       [4, 5]])

# set the column names of the named_array
A.set_colnames(['a1', 'b1', 'c1'])

# you can also put a numpy array into the name_array constructor
# and turn it into a named_array
B = np.array([[1,2,3],[4,5,6]])
C = named_array(B, colnames=['a', 'b', 'c'])

# the column name could also be a tuple, where the first element is the column name,
# the second element is the number of columns the column name spans
A = named_array([[1,2,3],[4,5,6]], colnames=['a', ('b', 2)])
>>> A['b']
named_array([[2, 3],
             [5, 6]])
```

