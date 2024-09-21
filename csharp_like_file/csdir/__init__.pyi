import os as _os
import pathlib as _pathlib


def create_directory(path: str | _os.PathLike[str],
                     unix_create_mode: int = 0o777) -> _pathlib.Path:
    result = _pathlib.Path(path)
    result.mkdir(mode=unix_create_mode, parents=True, exist_ok=True)
    return result
