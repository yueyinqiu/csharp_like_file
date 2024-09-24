import os as _os
import typing as _typing


def append_all_lines(path: str | _os.PathLike[str],
                     contents: _typing.Iterable[str],
                     encoding: str = "utf8") -> None:
    with open(path, "a", encoding=encoding, newline=None) as file:
        iterator = iter(contents)

        line = next(iterator)
        file.write(line)

        for line in iterator:
            file.write("\n")
            file.write(line)


def append_all_text(path: str | _os.PathLike[str],
                    contents: str,
                    encoding: str = "utf8") -> None:
    with open(path, "a", encoding=encoding, newline="") as file:
        file.write(contents)


def copy(source_file_name: str | _os.PathLike[str],
         dest_file_name: str) -> None:
    import shutil
    shutil.copyfile(source_file_name, dest_file_name)


def delete(path: str | _os.PathLike[str]) -> None:
    _os.remove(path)


def exists(path: str | _os.PathLike[str] | None) -> bool:
    if path is None:
        return False
    return _os.path.exists(path)


def move(source_file_name: str | _os.PathLike[str],
         dest_file_name: str | _os.PathLike[str]) -> None:
    import shutil
    shutil.move(source_file_name, dest_file_name)


def read_all_bytes(path: str | _os.PathLike[str]) -> bytes:
    with open(path, "rb") as file:
        return file.read()


def read_all_lines(path: str | _os.PathLike[str],
                   encoding: str = "utf8") -> list[str]:
    with open(path, "r", encoding=encoding, newline=None) as file:
        return [line.rstrip("\n") for line in file.readlines()]


def read_all_text(path: str | _os.PathLike[str],
                  encoding: str = "utf8") -> str:
    with open(path, "r", encoding=encoding, newline="") as file:
        return file.read()


def write_all_bytes(path: str | _os.PathLike[str],
                    bytes_: bytes) -> None:
    with open(path, "wb") as file:
        file.write(bytes_)


def write_all_lines(path: str | _os.PathLike[str],
                    contents: _typing.Iterable[str],
                    encoding: str = "utf8") -> None:
    with open(path, "w", encoding=encoding, newline=None) as file:
        iterator = iter(contents)

        line = next(iterator)
        file.write(line)

        for line in iterator:
            file.write("\n")
            file.write(line)


def write_all_text(path: str | _os.PathLike[str],
                   contents: str,
                   encoding: str = "utf8") -> None:
    with open(path, "w", encoding=encoding, newline="") as file:
        file.write(contents)
