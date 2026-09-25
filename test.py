
import numpy as np


array = np.array([[11, 2, 4], 
                  [4, 5, 6], 
                  [10, 8, -12]])

primary_diag = np.trace(array)
secondary_diag = np.trace(np.fliplr(array))

higher = max(primary_diag, secondary_diag)
lower = min(primary_diag, secondary_diag)

result = higher - lower

print(result)


