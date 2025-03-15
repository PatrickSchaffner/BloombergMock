from bloomberg._mocker import Mocker
_mkf = Mocker('xbbg.blp').create_function

__version__ = None

connect = _mkf('connect')
bdp = _mkf('bdp')
bdh = _mkf('bdh')
bds = _mkf('bds')
bdib = _mkf('bdib')
bdtick = _mkf('bdtick')
earning = _mkf('earning')
beqs = _mkf('beqs')
live = _mkf('live')
subscribe = _mkf('subscribe')
adjust_ccy = _mkf('adjust_ccy')
turnover = _mkf('turnover')
