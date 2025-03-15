from importlib import import_module
from pathlib import Path
import sys
from typing import Any, Callable


_import_errors: dict[str,ImportError] | None = None


def initialize_packages():
    global _import_errors
    if _import_errors is not None:
        return
    _import_errors = dict()

    mock_dir = Path(__file__).parent / 'mock'
    for pkg in mock_dir.iterdir():
        if not pkg.is_dir() or pkg.name.startswith('_'):
            continue
        try:
            import_module(pkg.name)
        except ImportError as e:
            _import_errors[pkg.name] = e
    if len(_import_errors) > 0:
        sys.path.append(str(mock_dir))


def _raise_error(module: str) -> None:
    global _import_errors
    pkg = module.split('.')[0]
    if pkg in _import_errors:
        raise _import_errors[pkg]
    else:
        raise ImportError(name=module)


class Mocker:

    def __init__(self, module: str) -> None:
        self._module = module

    def create_function(self, name: str) -> Callable[[Any,...], Any]:
        def _impl(*_1, **_2) -> None:
            _raise_error(self._module)
        return _impl

    def create_class(self, name: str) -> type:
        class _ClsImpl:
            def __init__(_1, *_2, **_3) -> None:
                _raise_error(self._module)
        cls = type(name, (_ClsImpl,), {})
        return cls
