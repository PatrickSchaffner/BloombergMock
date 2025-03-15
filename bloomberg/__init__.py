from importlib.resources import read_text

__version__ = read_text(__name__, 'version.txt').strip()

from .mocker import initialize_packages as _init
_init()
