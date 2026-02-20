import os as _os
import pathlib as _pathlib

import csfile as _csfile


def create_directory(path: str | _os.PathLike[str],
                     unix_create_mode: int = 0o777,
                     lexical: bool = False) -> _pathlib.Path:
    path = _csfile._resolve_path(path, lexical)
    result = _pathlib.Path(path)
    result.mkdir(mode=unix_create_mode, parents=True, exist_ok=True)
    return result
