# Converts the input into a complex number and prints its modulus r and phase angle phi
# using cmath.

import cmath
z = complex(input())
r = cmath.polar(z)[0]
phi = cmath.phase(z)
print(r)
print(phi)