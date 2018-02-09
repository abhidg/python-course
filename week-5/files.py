from pathlib import Path

# A Path variable points to a folder or a file
# Here it points to the file hello.txt in the current folder
fn = Path('hello.txt')

# Calling read text on the path object loads the
# contents of the file into a string
s = fn.read_text()

#  You can also replace the contents of a file by using write text
fn.write_text('this will replace whatever is in the file')

# Often you will want to loop through the lines in a file,
# for that you have two first open the file and then loop.
with fn.open() as fp:  # Here fp is a file object
    for i in fp.readlines():
        pass

# For example, count the number of words in the file
words = 0
with fn.open() as fp:  # Here fp is a file object
    for i in fp.readlines():
	    words += len(i.split())

d = Path('.')  # . is always the current directory
print(list(d.glob('*.txt'))) # Returns all .txt files in the current directory

# Point to something subfolder within the current directory
subfolder = d / 'something'

# Check that it exists, otherwise create it
if not subfolder.exists():
    subfolder.mkdir()

(d / 'something' / 'else.txt').write_text('entirely')
