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

from pandas.tseries.offsets import DateOffset
from bloomberg.api.pandas.tseries import offsets
assert DateOffset is pd.tseries.offsets.DateOffset
assert DateOffset is offsets.DateOffset
assert DateOffset is bloomberg.api.pandas.tseries.offsets.DateOffset
print(DateOffset)

