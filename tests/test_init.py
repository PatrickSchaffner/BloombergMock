import re


def test_version():
    from bloomberg import __version__
    assert re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', __version__)
