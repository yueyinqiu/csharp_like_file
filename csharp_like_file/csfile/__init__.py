import os as _os
import typing as _typing


def append_all_lines(path: str,
                     contents: _typing.Iterable[str],
                     encoding: str = "utf8") -> None:
    with open(path, "a", encoding=encoding) as file:
        file.writelines(contents)


def append_all_text(path: str,
                    contents: str,
                    encoding: str = "utf8") -> None:
    with open(path, "a", encoding=encoding) as file:
        file.write(contents)


def copy(source_file_name: str,
         dest_file_name: str) -> None:
    import shutil
    shutil.copyfile(source_file_name, dest_file_name)


def delete(path: str) -> None:
    _os.remove(path)


def exists(path: str | None) -> None:
    _os.path.exists(path)


def move(source_file_name: str,
         dest_file_name: str) -> None:
    import shutil
    shutil.move(source_file_name, dest_file_name)


def read_all_bytes(path: str) -> bytes:
    with open(path, "rb") as file:
        return file.read()


def read_all_lines(path: str,
                   encoding: str = "utf8") -> list[str]:
    with open(path, "r", encoding=encoding) as file:
        return file.readlines()


def read_all_text(path: str,
                  encoding: str = "utf8") -> str:
    with open(path, "r", encoding=encoding) as file:
        return file.read()


def read_lines(path: str,
               encoding: str = "utf8") -> _typing.Iterable[str]:
    with open(path, "r", encoding=encoding) as file:
        for line in file.readline():
            if line is None:
                break
            yield line


def write_all_bytes(path: str,
                    bytes_: bytes) -> None:
    with open(path, "wb") as file:
        file.write(bytes_)


def write_all_lines(path: str,
                    contents: _typing.Iterable[str],
                    encoding: str = "utf8") -> None:
    with open(path, "w", encoding=encoding) as file:
        file.writelines(contents)


def write_all_text(path: str,
                   contents: str,
                   encoding: str = "utf8") -> None:
    with open(path, "w", encoding=encoding) as file:
        file.write(contents)
