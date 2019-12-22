# 2. Create lambda functions that calculate `pow`, `sum`, and `multiply`.
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 33]))
print(reduce(lambda x, y: x * y, [3, 10]))
print(reduce(lambda x, y: x ** y, [2, 2]))

