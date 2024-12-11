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

