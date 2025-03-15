from bloomberg._mocker import Mocker


_m = Mocker('pandas.tseries.offsets')
_mkc = _m.create_class


DateOffset = _mkc('DateOffset')
