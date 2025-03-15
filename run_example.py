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

from pandas.tseries.offsets import DateOffset
from bloomberg.pandas.tseries import offsets

assert DateOffset is pd.tseries.offsets.DateOffset
assert DateOffset is offsets.DateOffset
assert DateOffset is bloomberg.pandas.tseries.offsets.DateOffset
print(DateOffset)

print(DataFrame())
print(bloomberg.xbbg.blp.bdh())
