import sys
import time

seconds = int(sys.argv[-1])

for _ in range(seconds):
    print(time.ctime())
    time.sleep(1)
