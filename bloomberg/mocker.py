from typing import Any, Callable

from . import api


def _raise_error(module: str) -> None:
    pkg = module.split('.')[0]
    if pkg in api.import_errors:
        raise api.import_errors[pkg]
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
