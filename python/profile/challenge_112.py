
import os.path
import sys
import time
sys.path.append(os.path.abspath(os.path.join('.', os.path.pardir)))

import challenge_112_easy as lib

start = time.time()
for i in range(0, 10000):
	lib.main('http://en.wikipedia.org/w/index.php?title=Main_Page&action=edit')
end = time.time()
print end - start

