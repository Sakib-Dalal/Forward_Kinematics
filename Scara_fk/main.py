import numpy as np


# input angles in radians 
q1 = 0.0 # base_arm_motor
q2 = 0.0 # arm_motor
q3 = 0.0 # shaft_linear_motor


# given vectors - course work given 
# From base to joint 1 
base_x = 0.060
base_y= 0.000
base_z = 0.220

# From joint 1 to joint 2
length1_x = 0.310
length1_y = 0.005
length1_z = -0.004

# From joint 2 to TCP
length2_x = 0.2545
length2_y = -0.005
length2_z = q3 - 0.034

# Finding x, y, z coordinates
# Position_TCP = P_base + Rz(q1)length1 + Rz(q1+q2)length2

# x coordinates 
x = base_x + np.cos(q1) * length1_x - np.sin(q1) * length1_y + np.cos(q1+q2) * length2_x - np.sin(q1+q2) * length2_y

print(x)

# y coordinates
y = base_y + np.sin(q1) * length1_x + np.cos(q1) * length1_y + np.sin(q1+q2) * length2_x + np.cos(q1+q2) * length2_y

print(y)

# z coordinates
z = base_z + length1_z + length2_z

print(z)
