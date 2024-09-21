I really appreciate the design of `System.IO.File` and `System.IO.Directory`, which provides many static methods to access the file system easily.

This project is mainly to meet my use so I didn't write it so seriously. If there are any bugs or if you'd like some new features, please feel free to contact me in the issues, although it might be many years after the last commit. I believe I would give a response if I'm still alive.

An example:

```python
import csdir
import csfile

directory = csdir.create_directory("test")  # It's a pathlib.Path
csfile.write_all_text(directory / "test.txt", "Hello World")
```
