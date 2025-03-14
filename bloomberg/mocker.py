from importlib import import_module
from pathlib import Path
import sys


_initialized: bool = False


def initialize_packages():
    global _initialized
    if _initialized:
        return
    mock_dir = Path(__file__).parent / 'mock'
    import_error = False
    for pkg in mock_dir.iterdir():
        if not pkg.is_dir() or pkg.name.startswith('_'):
            continue
        try:
            import_module(pkg.name)
        except ImportError:
            import_error = True
    if import_error:
        sys.path.append(str(mock_dir))
    _initialized = True
