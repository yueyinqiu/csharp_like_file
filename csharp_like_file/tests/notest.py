import csdir
import csfile

directory = csdir.create_directory("test")  # It's a pathlib.Path
csfile.write_all_text(directory / "test.txt", "Hello World")
