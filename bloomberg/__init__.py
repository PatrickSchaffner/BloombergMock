from importlib.resources import read_text
import sys


__version__ = read_text(__name__, 'version.txt').strip()

from . import api

# Provide subpackages as package attributes.
__all__ = ['xbbg', 'pandas']
xbbg = sys.modules[f'{api.__name__}.xbbg']
pandas = sys.modules[f'{api.__name__}.pandas']
