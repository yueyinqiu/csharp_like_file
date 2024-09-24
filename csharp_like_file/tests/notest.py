import csdir
import csfile

directory = csdir.create_directory("test")
csfile.write_all_lines(directory / "test.txt", "Hello World")
text = csfile.read_all_text(directory / "test.txt")
qwq = csfile.read_all_lines(directory / "test.txt")
pass
