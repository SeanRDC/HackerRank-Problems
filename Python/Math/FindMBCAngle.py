# Uses atan2 on sides AB and BC to get angle MBC in radians, converts it to degrees,
# rounds it, and prints it with a degree sign.

import math
ab = int(input())
bc = int(input())
print(f"{round(math.degrees(math.atan2(ab, bc)))}{chr(176)}")