from bloomberg.api.pandas.tseries.offsets import DateOffset
import bloomberg

import pandas as pd
import bloomberg.api.pandas as pd2
assert pd is pd2
assert pd is bloomberg.api.pandas
print(pd)
print(pd2)

from bloomberg.api.pandas import DataFrame
assert DataFrame is pd2.DataFrame
assert DataFrame is pd.DataFrame
assert DataFrame is bloomberg.api.pandas.DataFrame
print(DataFrame)

from pandas.tseries import offsets

assert DateOffset is pd.tseries.offsets.DateOffset
assert DateOffset is offsets.DateOffset
assert DateOffset is bloomberg.api.pandas.tseries.offsets.DateOffset
print(DateOffset)
print(DateOffset.__module__)
print(DateOffset.__name__)
print(DateOffset.__qualname__)

print(DataFrame)
print(DataFrame.__module__)
print(DataFrame.__name__)
print(DataFrame.__qualname__)

print(bloomberg.api.xbbg.blp.bdh.__qualname__)
print(bloomberg.api.xbbg.blp.bdh.__module__)
print(bloomberg.api.xbbg.blp.bdh)

print(DataFrame())
print(bloomberg.api.xbbg.blp.bdh())