from bloomberg.pandas.tseries.offsets import DateOffset
import bloomberg

import pandas as pd
import bloomberg.pandas as pd2
assert pd is pd2
assert pd is bloomberg.pandas
print(pd)
print(pd2)

from bloomberg.pandas import DataFrame
assert DataFrame is pd2.DataFrame
assert DataFrame is pd.DataFrame
assert DataFrame is bloomberg.pandas.DataFrame
print(DataFrame)

from pandas.tseries import offsets

assert DateOffset is pd.tseries.offsets.DateOffset
assert DateOffset is offsets.DateOffset
assert DateOffset is bloomberg.pandas.tseries.offsets.DateOffset
print(DateOffset)
print(DateOffset.__module__)
print(DateOffset.__name__)
print(DateOffset.__qualname__)

print(DataFrame)
print(DataFrame.__module__)
print(DataFrame.__name__)
print(DataFrame.__qualname__)

print(bloomberg.xbbg.blp.bdh.__qualname__)
print(bloomberg.xbbg.blp.bdh.__module__)
print(bloomberg.xbbg.blp.bdh)

print(DataFrame())
print(bloomberg.xbbg.blp.bdh())