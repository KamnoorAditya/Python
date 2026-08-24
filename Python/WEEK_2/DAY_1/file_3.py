import sys
from datetime import datetime
now=datetime.now()

file=open("date.py","w")
file.write("""from datetime import datetime\nprint(datetime.now())""")
file.close()