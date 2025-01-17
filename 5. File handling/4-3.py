# Note that some file operations may cause the program to stop working (e.g. there is no file on the disk with the given name).
# To prevent this, you can use the try-except block to handle exceptions,
# which are errors that can occur during the execution of a program. Exceptions might arise, for example,
# when attempting to divide by zero, accessing a non-existent file, or processing data in the wrong format.

# The idea behind try-except is that you place the code that might cause an error inside the try block,
# and if an error occurs, the except block handles it without crashing the program.

# try:
#    # code that may raise exceptions
# except ExceptionType:
#    # code to handle the exception

# The program read_file.py. tries to print the contents of a file that is not on the disk.
# Read the contents of the program. Then run the program and see what happens.
#  As you can see, the program stops when it encounters an error (attempting to open a nonexistent file).

# Next, see the contents of the program read_file_try_except.py, which opens and reads the contents of a file inside a
# try-except block. Finally, run the program. As you can see, even when an error occurs (attempting to open a nonexistent file),
# the program continues to run.