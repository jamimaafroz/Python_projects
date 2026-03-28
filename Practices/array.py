import numpy as np
import time

start = time.time()

for _ in range(100000):
    np.arange(1, 9)**4

end = time.time()

print("Time taken:", end - start)