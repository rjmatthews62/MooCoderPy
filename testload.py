import sys,os
fullpath=os.path.abspath("src")
sys.path.insert(1,fullpath)
import MooCoderPy
print(MooCoderPy.__VERSION__)
print(MooCoderPy.__file__)
for x in sys.path: print(x)
import MooCoderPy.__main__
