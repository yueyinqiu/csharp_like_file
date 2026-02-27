# csharp-like-file

If you've ever used C# and found yourself missing the sheer convenience of `System.IO.File` and `System.IO.Directory`, you're not alone. I've always loved how those static methods make file operations feel so effortless, so I decided to bring that same "vibe" to Python.

I originally built this just to scratch my own itch, so it's not meant to be some over-engineered masterpiece. It's just a straightforward tool to help you get things done. If you run into a bug or realize I missed a standard C# method you can't live without, just give me a shout in the issues!

## Quick Example

```python
import csdir
import csfile

directory = csdir.create_directory("test_folder")  # This returns a pathlib.Path object
csfile.write_all_text(directory / "hello.txt", "Hello World")
```

## Differences from the C# Version

There are a couple of small "cultural" differences between Python and C# that you should know about.

### Encoding (`encoding`)

I've set the default text encoding to UTF-8. I'm not a big fan of C#'s `Encoding.Default` (which can be a bit unpredictable depending on your OS). You can always pass your own encoding parameter if you need something specific.

### Path Resolution

In C#, a path like `a/b/..` is usually treated as a pure string operation. In that world, it always simplifies to `a`. But sometimes, if `b` is actually a symlink pointing somewhere else, you may expect that `..` should take you to the real parent of that target.

However, the meaning of `delete` and `exist` clear, we kept the C# behavior. Therefore, when you call `delete` on a symlink file, it will certainly removing the symlink itself, rather than its destination. If you want to resolve the symlinks, call `pathlib.Path.resolve` or `os.path.realpath` before passing the paths into this package.
