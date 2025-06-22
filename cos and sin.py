import math


A_deg = 29
B_deg = 68
b = 27


C_deg = 180 - A_deg - B_deg


A_rad = math.radians(A_deg)
B_rad = math.radians(B_deg)
C_rad = math.radians(C_deg)

a = (b * math.sin(A_rad)) / math.sin(B_rad)


area = 0.5 * a * b * math.sin(C_rad)

print(f"Area of the triangle: {area:.5f} square mm")
