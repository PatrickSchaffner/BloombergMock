from bloomberg.mocker import Mocker
_mkf = Mocker('xbbg.pipeline').create_function

__version__ = None

get_series = _mkf('get_series')
standard_cols = _mkf('standard_cols')
apply_fx = _mkf('apply_fx')
daily_stats = _mkf('daily_stats')
dropna = _mkf('dropna')
format_raw = _mkf('format_raw')
add_ticker = _mkf('add_ticker')
since_year = _mkf('since_year')
perf = _mkf('perf')
