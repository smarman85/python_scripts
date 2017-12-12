import time
import sys
some_values = list(range(1,101))
for item in some_values:
    time.sleep(5)
    progress = (some_values.index(item) + 1 ) / len(some_values) * 100
    sys.stdout.write("Percent complete: %d%% \r" % (progress) )
    sys.stdout.flush()

print (len(some_values))


