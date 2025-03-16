from bloomberg.mocker import Mocker

_m = Mocker('pandas')
_mkc = _m.create_class


DataFrame = _mkc('DataFrame')
