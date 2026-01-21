##MATH MODULE

#square root of 625

import math
print("Square root is :",math.sqrt(625))


#factorial of 6

print("Factorial of 6 is :", math.factorial(6))


#floor and ceiling value of 4.7
print("Floor of 4.7 is :", math.floor(4.7))
print("Ceil of 4.7 is :", math.ceil(4.7))

#compute 5 and raised the power 3 the math module

print("Power of num:", math.pow(5,3))


#find the absolute value of -18  using math fabs

print("The absolute value of -18 is :", math.fabs(-18))

#find the sine cosine and tangent of 90 defree(convert degree to radians)

degrees = 90
radians = math.radians(degrees)
sine_val = math.sin(radians)
cosine_val = math.cos(radians)
tangent_val = math.tan(radians)
print(f"Sine of 90 degrees: {sine_val}")
print(f"Cosine of 90 degrees: {cosine_val}")
print(f"Tangent of 90 degrees: {tangent_val}")


# 36 aur 60 ka GCD nikalna
gcd_value = math.gcd(36, 60)
print("GCD:", gcd_value)

# e power 3 calculate karna
e_power_3 = math.e ** 3
print("e^3:", e_power_3)

# 1000 ka base 10 logarithm
log_value = math.log10(1000)
print("log10(1000):", log_value)

# 180 degrees ko radians me convert karna
radian_value = math.radians(180)
print("180 degrees in radians:", radian_value)