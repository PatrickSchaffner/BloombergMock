
def test_xbbg():
    import xbbg

    from xbbg import blp
    from xbbg import pipeline
    from xbbg import const

    from xbbg.blp import __version__
    from xbbg.blp import bdh
    from xbbg.blp import bdp
    from xbbg.blp import bds
    from xbbg.blp import connect
    from xbbg.blp import bdib
    from xbbg.blp import bdtick
    from xbbg.blp import earning
    from xbbg.blp import beqs
    from xbbg.blp import live
    from xbbg.blp import subscribe
    from xbbg.blp import adjust_ccy
    from xbbg.blp import turnover

    from xbbg.const import Futures
    from xbbg.const import CurrencyPair
    from xbbg.const import ValidSessions
    from xbbg.const import exch_info
    from xbbg.const import market_info
    from xbbg.const import take_first
    from xbbg.const import asset_config
    from xbbg.const import explode
    from xbbg.const import ccy_pair
    from xbbg.const import market_timing

    from xbbg.pipeline import get_series
    from xbbg.pipeline import standard_cols
    from xbbg.pipeline import apply_fx
    from xbbg.pipeline import daily_stats
    from xbbg.pipeline import dropna
    from xbbg.pipeline import format_raw
    from xbbg.pipeline import add_ticker
    from xbbg.pipeline import since_year
    from xbbg.pipeline import perf


def test_bloomberg_xbbg():
    import bloomberg
    import xbbg
    from bloomberg.xbbg import blp
    from bloomberg.xbbg.blp import bdh

    assert xbbg is bloomberg.xbbg
    assert xbbg.blp is bloomberg.xbbg.blp
    assert xbbg.blp is blp
    assert xbbg.blp.bdh is bloomberg.xbbg.blp.bdh
    assert xbbg.blp.bdh is blp.bdh
    assert xbbg.blp.bdh is bdh
