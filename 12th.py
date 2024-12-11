a = bool(123)
print(a) # 
print(type(a))

a = bool(0)
print(a)
print(type(a))
a = bool(-245)
print(a)

a = bool(None)    #    bool( 0, 0.0, None, '' ,"")           False 
print(a)







def burger_maker():
    print("Need 2 buns")
    print("Add cheese")
    print("Add patty")
    print("Add Sauces")
    print("Burger is ready")
    

def pizza_maker():
    print("Need pizza base")
    print("Add cheese")
    print("Add Mushrooms")
    print("Add onion")
    print("Pizza is ready")
    

# Orders are coming

# Pizza
pizza_maker()
print()
# Burger
burger_maker()
print()
# Pizza
pizza_maker()
print()
# Burger
burger_maker()

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data
de_broglie_lambda = [25.064, 24.081, 22.418, 20.465, 19.414, 18.511, 17.365]
λ_1 = [25.108, 24.444, 22.269, 20.619, 19.333, 18.619, 17.738]
λ_2 = [25.649, 24.342, 22.953, 20.807, 19.851, 18.6, 17.642]

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Scatter plot for de_broglie_lambda vs λ_1
ax1.scatter(de_broglie_lambda, λ_1, color='blue', label='Data points')
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(de_broglie_lambda, λ_1)
line1 = slope1 * np.array(de_broglie_lambda) + intercept1
ax1.plot(de_broglie_lambda, line1, color='red', label='Fitted line')
ax1.set_xlabel('de_broglie_lambda')
ax1.set_ylabel('λ_1')
ax1.set_title('de_broglie_lambda vs λ_1')
ax1.legend()

# Scatter plot for de_broglie_lambda vs λ_2
ax2.scatter(de_broglie_lambda, λ_2, color='green', label='Data points')
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(de_broglie_lambda, λ_2)
line2 = slope2 * np.array(de_broglie_lambda) + intercept2
ax2.plot(de_broglie_lambda, line2, color='red', label='Fitted line')
ax2.set_xlabel('de_broglie_lambda')
ax2.set_ylabel('λ_2')
ax2.set_title('de_broglie_lambda vs λ_2')
ax2.legend()

plt.tight_layout()
plt.show()

# Print statistics for de_broglie_lambda vs λ_1
print("Statistics for de_broglie_lambda vs λ_1:")
print(f"Slope: {slope1:.4f}")
print(f"Intercept: {intercept1:.4f}")
print(f"Standard Error: {std_err1:.4f}")

print("\nStatistics for de_broglie_lambda vs λ_2:")
print(f"Slope: {slope2:.4f}")
print(f"Intercept: {intercept2:.4f}")
print(f"Standard Error: {std_err2:.4f}")





