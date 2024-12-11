pip install matplotlib pandas
conda install -c conda-forge matplotlib pandas
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame from the provided data
data = {
    'voltage(V)_1': [1.069, 1.067, 1.066, 1.065, 1.063, 1.061, 1.058, 1.053, 1.044, 1.017, 0.582, 0.622, 0.54, 0.54, 0.42, 0.3, 0.1],
    'current(mA)_1': [14, 15, 16, 18, 20, 23, 27, 34, 46, 76, 164, 163, 164, 164, 164, 165, 166],
    'voltage(V)_2': [1.023, 1.022, 1.021, 1.019, 1.015, 1.01, 1.003, 0.987, 0.956, 0.806, 0.234, 0.234, 0.211, 0.21, 0.155, 0.102, 0.036],
    'current(mA)_2': [13, 14, 16, 17, 19, 22, 26, 32, 42, 61, 67, 67, 67, 67, 67, 67, 67],
    'voltage(V)_3': [0.996, 0.993, 0.99, 0.985, 0.979, 0.97, 0.953, 0.921, 0.832, 0.565, 0.156, 0.156, 0.14, 0.126, 0.092, 0.052, 0.022],
    'current(mA)_3': [13, 14, 15, 17, 19, 21, 25, 30, 38, 44, 45, 45, 45, 45, 45, 45, 45],
    'voltage(V)_4': [0.856, 0.844, 0.826, 0.8, 0.766, 0.716, 0.628, 0.524, 0.386, 0.225, 0.058, 0.058, 0.055, 0.048, 0.038, 0.025, 0.007],
    'current(mA)_4': [12, 12, 13, 14, 15, 16, 17, 18, 18, 19, 19, 19, 19, 19, 19, 19, 18],
    'voltage(V)_5': [0.415, 0.388, 0.356, 0.324, 0.286, 0.246, 0.202, 0.156, 0.109, 0.065, 0.016, 0.016, 0.015, 0.013, 0.012, 0.009, 0.003],
    'current(mA)_5': [7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 5]
}

df = pd.DataFrame(data)

# Plot the V-I graphs
plt.figure(figsize=(16, 10))

# Plot each graph with a different label
plt.plot(df['voltage(V)_1'], df['current(mA)_1'], label='Frosted', marker='o')
plt.plot(df['voltage(V)_2'], df['current(mA)_2'], label='Frosted+Attenuator_1', marker='s')
plt.plot(df['voltage(V)_3'], df['current(mA)_3'], label='Frosted+Attenuator_2', marker='^')
plt.plot(df['voltage(V)_4'], df['current(mA)_4'], label='Frosted+Attenuator_3', marker='d')
plt.plot(df['voltage(V)_5'], df['current(mA)_5'], label='Frosted+Attenuator_4', marker='x')

# Add labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('V-I Graph for Multiple Voltage-Current Pairs')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# adding a new file
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame with padding to equalize column lengths
data = {
    'voltage(V)_1': [-0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1,  0. ,  0.1,  0.2,  0.3, 0.4,  0.5,  0.6,  0.7],
    'current(mA)_1': [0.002     , 0.002     , 0.002     , 0.002     , 0.002     ,0.003     , 0.003     , 0.003     , 0.003     , 0.003     ,0.005     , 0.014     , 0.065     , 0.26366667, 0.593 ],
    'voltage(V)_2': [-0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
    'current(mA)_2': [-0.217, -0.218, -0.217, -0.216, -0.216, -0.217, -0.217, -0.217, -0.216, -0.214, -0.206, -0.156, -0.025, 0.365, 0.764],
    'voltage(V)_3': [0.53, 0.53, 0.53, 0.529, 0.529, 0.528, 0.527, 0.525, 0.52, 0.474, 0.469, 0.462, 0.43, 0.224, 0.126],
    'current(mA)_3': [8, 9, 10, 11, 13, 15, 18, 25, 41, 137, 144, 154, 178, 213, 214],
    'voltage(V)_4': [1.074, 1.072, 1.071, 1.07, 1.068, 1.066, 1.062, 1.054, 1.033, 0.729, 0.723, 0.613, 0.541, 0.417, 0.219],
    'current(mA)_4': [14, 16, 18, 20, 23, 27, 35, 47, 79, 206, 208, 210, 211, 212, 213],
    'voltage(V)_5': [0.544, 0.542, 0.541, 0.54, 0.539, 0.539, 0.537, 0.534, 0.516, 0.514, 0.51, 0.496, 0.49, 0.452, 0.223],
    'current(mA)_5': [8, 9, 10, 11, 15, 18, 25, 43, 143, 154, 174, 228, 249, 346, 430]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Plot the V-I graphs with labels
plt.figure(figsize=(10, 6))

# Plot each graph with a different label
plt.plot(df['voltage(V)_1'], df['current(mA)_1'], label='Dark IV', marker='o')
plt.plot(df['voltage(V)_2'], df['current(mA)_2'], label='Bright', marker='s')
plt.plot(df['voltage(V)_3'], df['current(mA)_3'], label='Resistance', marker='^')
plt.plot(df['voltage(V)_4'], df['current(mA)_4'], label='Series', marker='d')
plt.plot(df['voltage(V)_5'], df['current(mA)_5'], label='Parallel', marker='x')

# Set labels and title
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('V-I Graph Comparison')
# Add a legend
plt.legend()
# Show the plot
plt.show()

import matplotlib.pyplot as plt

# Data for falling temperature phase
temp_falling_C = [274, 286, 350, 375, 400, 422, 450, 474, 500, 525, 550, 574, 600, 625, 650, 675, 690]
current_falling = [0.2, 0.4, 3.3, 6.0, 11.0, 18.0, 33.5, 56.1, 94.0, 155.0, 262.0, 444.0, 1012.0, 1750.0, 2663.0, 4170.0, 4700.0]

# Data for rising temperature phase
temp_rising_C = [50, 100, 150, 200, 250, 300, 350, 390, 400, 425, 450, 475, 500, 525, 550, 585, 600, 625, 650, 675, 689]
current_rising = [446, 488, 39.6, 0, 0, 0, 0.1, 1.1, 1.2, 2.6, 4.0, 7.0, 13.5, 25.2, 40.0, 95.0, 140.0, 280.0, 745.0, 1335.0, 3486.0]

# Plotting the data
plt.figure(figsize=(10,6))

# Plot for falling temperature phase
plt.plot(temp_falling_C, current_falling, label="Falling Temperature", marker='o', linestyle='-')

# Plot for rising temperature phase
plt.plot(temp_rising_C, current_rising, label="Rising Temperature", marker='x', linestyle='--')

# Adding labels and title
plt.xlabel("Temperature (°C)")
plt.ylabel("Current (µA)")
plt.title("Ionic Conductivity: Current vs Temperature")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
