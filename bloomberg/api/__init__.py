from importlib import import_module
from pathlib import Path
import sys
from logging import getLogger


mock_dir = Path(__file__).parent
import_errors: dict[str,ImportError] = dict()


# Try to load real packages and replace mock subpackages.
# Every subpackage of bloomberg is considered a target top-level package.
for pkg in mock_dir.iterdir():
    if not pkg.is_dir() or pkg.name.startswith('_'):
        continue
    try:
        impl = import_module(pkg.name)  # import xbbg
        sys.modules[f'{__name__}.{pkg.name}'] = impl  # bloomberg.api.xbbg = xbbg
    except ImportError as e:
        # Remember unavailable packages, and store ImportError for mock API.
        import_errors[pkg.name] = e

# Recurse a directory and collect the names of all provided packages and modules.
# Modules and subpackages are returned after their containing package.
def _walk_pkg_dir(base: str, pkg_dir: Path):
    yield base
    for f in pkg_dir.iterdir():
        if f.name.startswith('_'):
            continue
        if f.is_file() and f.name.endswith('.py'):  # Module
            yield f"{base}.{f.name[:-3]}"
            continue
        if f.is_dir() and (f / '__init__.py').is_file():  # Subpackage
            sub_pkg = f"{base}.{f.name}"
            yield from _walk_pkg_dir(sub_pkg, f)
            continue

# If some real packages are missing, insert mocks into sys.path
if len(import_errors) > 0:

    # Add bloomberg package directory to sys.path
    # Already loaded packages will not be affected.
    # Missing packages are redirected to bloomberg subpackages on import.
    # WARNING: This will insert all elements onto sys.path. Only add mocks to this project.
    sys.path.append(str(mock_dir))

    # Load mock packages
    for pkg in import_errors.keys():
        try:
            for mod in _walk_pkg_dir(base=pkg, pkg_dir=mock_dir / pkg):  # Import top-level and nested packages/modules.
                impl = import_module(mod)  # import xbbg.blp -> sys.path entry matches.
                sys.modules[f"{__name__}.{mod}"] = impl  # bloomberg.api.xbbg.blp = xbbg.blp (prevent copy of mock package)
        except ImportError as e:
            log = getLogger(__name__)
            log.error('Could not import mocked package.', e)
