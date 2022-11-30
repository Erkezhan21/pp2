import math

def vol(rad):
    v = float( 3.14 * (rad**3) * (4/3))
    return v

rad = int(input())
print(vol(rad))