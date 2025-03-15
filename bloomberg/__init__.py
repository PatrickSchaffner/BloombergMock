from importlib.resources import read_text
from importlib import import_module
from pathlib import Path
import sys
from logging import getLogger


__version__ = read_text(__name__, 'version.txt').strip()


root_dir = Path(__file__).parent
import_errors: dict[str,ImportError] = dict()

for pkg in root_dir.iterdir():
    if not pkg.is_dir() or pkg.name.startswith('_'):
        continue
    try:
        impl = import_module(pkg.name)
        sys.modules[f'bloomberg.{pkg.name}'] = impl
    except ImportError as e:
        import_errors[pkg.name] = e


def _walk_pkg_dir(base: str, pkg_dir: Path):
    yield base
    for f in pkg_dir.iterdir():
        if f.name.startswith('_'):
            continue
        if f.is_file() and f.name.endswith('.py'):
            yield f"{base}.{f.name[:-3]}"
            continue
        if f.is_dir() and (f / '__init__.py').is_file():
            sub_pkg = f"{base}.{f.name}"
            yield from _walk_pkg_dir(sub_pkg, f)
            continue

if len(import_errors) > 0:
    sys.path.append(str(root_dir))
    log = getLogger(__name__)
    for pkg in import_errors.keys():
        try:
            for module in _walk_pkg_dir(base=pkg, pkg_dir=root_dir / pkg):
                impl = import_module(module)
                sys.modules[f"bloomberg.{module}"] = impl
        except ImportError as e:
            log.error('Could not import mocked package.', e)


__all__ = ['xbbg', 'pandas']
xbbg = sys.modules[f'{__name__}.xbbg']
pandas = sys.modules[f'{__name__}.pandas']
