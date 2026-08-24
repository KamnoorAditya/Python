from pathlib import Path
import sys
files=Path(".").glob("*.py")
for file in files:
    print(file)
print(sys.argv)
from collections import Counter
a=[1,2,3,4,5,6,4]
print(Counter(a))
