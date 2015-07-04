'''
CLASS: Reading and Writing Files in Python
'''

'''
Before we begin: 
Understanding the Python environment and the concept of a working directory
'''

import sys  # sys is the 'System' module
import os   # operating system tools
from pprint import pprint  # Pretty printing

lesson_dir = "Lec02-GitAndPython/exercises"

if lesson_dir not in os.getcwd():
    raise Exception("NOTE: You should call this script within the `Lec02-GitAndPython/exercises` directory")

print sys.version   # Remember this??

print '''

What is a "Working Directory"?

    Whenever you use a relative file path it is joined with your current directory to create an absolute file path.
    That is, if my current working directory is `/home/example_user` and I use a relative file path of
    `example_directory/example_python_program`, then that is equivalent to using the absolute file path of
    `/home/example_user/example_directory/example_file_program`.

    The moral of the story: Always pay attention to the value of your current working directory so you're not wasting 
    your time debugging trivial Python IO errors with path lookup.

'''

print "Python loads files relative to its working directory:"
print os.getcwd()


print '''


What is the "path"?

    from Python docs
    A list of strings that specifies the search path for *modules* (i.e. stuff you call with import). 
    Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.
    As initialized upon program startup, the first item of this list, path[0], is the directory containing 
    the script that was used to invoke the Python interpreter. If the script directory is not available 
    (e.g. if the interpreter is invoked interactively or if the script is read from standard input), 
    path[0] is the empty string, which directs Python to search modules in the current directory first. 
    Notice that the script directory is inserted before the entries inserted as a result of PYTHONPATH.

    A program is free to modify the path for its own purposes.

    -------


    The concept of a path and working directory have similar usage in almost all programming languages. One notable exception is JavaScript
'''

print "My Python path:"
pprint(sys.path)

print "Directory this script was run from:", sys.path[0]

print '''
*Again*, pay attention the directories specified within the path. 

A very common error you will see if you haven't already:

```
ImportError: No module named ...
```

It's because you tried to import a module that could not be found within one of the above directories.

*Common Solution:*

- Make sure you're using the version of python you think you are 
  (Run the `which -a python` command in bash to see where the operating system looks up the `python` command).
- Make sure the package is installed

'''


'''
Part 1: Reading files
Note: 'rU' mode (read universal) converts different line endings into '\n'
*Also Note: the Data directory is three levels above us (../../../data)
'''

os.chdir('../../')

# read the whole file at once, return a single string
f = open('../data/drinks.csv', 'rU')
f.read()        # one big string including newlines
f.read()        # empty string
f.close()

# read one line at a time (entire file does not have to fit into memory)
f = open('../data/drinks.csv', 'rU')
f.readline()    # one string per line (including newlines)
f.readline()    # next line
f.close()

# read the whole file at once, return a list of lines
f = open('../data/drinks.csv', 'rU')
f.readlines()   # one list, each line is one string
f.close()

# use list comprehension to duplicate readlines without reading entire file at once
f = open('../data/drinks.csv', 'rU')
[row for row in f]
f.close()

# use a context manager to automatically close your file
with open('../data/drinks.csv', 'rU') as f:
    [row for row in f]

# split on commas to create a list of lists
with open('../data/drinks.csv', 'rU') as f:
    [row.split(',') for row in f]

# use the built-in csv module instead
import csv
with open('../data/drinks.csv', 'rU') as f:
    [row for row in csv.reader(f)]

# use next to grab the next row
with open('../data/drinks.csv', 'rU') as f:
    header = csv.reader(f).next()
    data = [row for row in csv.reader(f)]


'''
Part 2: Writing files
Note: 'wb' mode (write binary) is usually the recommended option
'''

# write a string to a file
nums = range(5)
with open('nums.txt', 'wb') as f:
    for num in nums:
        f.write(str(num) + '\n')

# convert a list of lists into a CSV file
output = [['col1', 'col2', 'col3'], [4, 5, 6]]
with open('example.csv', 'wb') as f:
    for row in output:
        csv.writer(f).writerow(row)

# use writerows to do this in one line
with open('example.csv', 'wb') as f:
    csv.writer(f).writerows(output)


print "Success!"

