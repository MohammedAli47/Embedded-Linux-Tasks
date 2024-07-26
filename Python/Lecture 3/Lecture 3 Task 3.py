import sys

print("Script name/path: %s" % sys.argv[0])
print("Number of Arguments: %d" % len(sys.argv))
print("Argument List: ", end='')
print([i for i in sys.argv])