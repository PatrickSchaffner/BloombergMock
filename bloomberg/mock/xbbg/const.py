from bloomberg.mocker import Mocker
_mkf = Mocker('xbbg.const').create_function

Futures = None
CurrencyPair = None
ValidSessions = None

exch_info = _mkf('exch_info')
market_info = _mkf('market_info')
take_first = _mkf('take_first')
asset_config = _mkf('asset_config')
explode = _mkf('explode')
ccy_pair = _mkf('ccy_pair')
market_timing = _mkf('market_timing')
