
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Define the data
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Air Freight (kg)': [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000],
        'Sea Freight (kg)': [100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000],
        'Road Freight (kg)': [75000, 80000, 85000, 90000, 95000, 100000, 105000, 110000, 115000, 120000, 125000, 130000],
        'Rail Freight (kg)': [25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000]}

# Step 2: Convert the data into a dataframe
df = pd.DataFrame(data)

# Step 3: Convert the first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Step 4: Create a figure and set the size
fig, ax = plt.subplots(figsize=(12, 8))

# Step 5: Calculate the max total value and set the y-axis limit and ticks
max_total_value = np.ceil(df.iloc[:, 1:].sum(axis=1).max() / 1000) * 1000
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Step 6: Use ax.stackplot() to plot the chart
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3], df.iloc[:, 4], labels=['Air Freight', 'Sea Freight', 'Road Freight', 'Rail Freight'], colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'], alpha=0.8)

# Step 7: Set the labels, title, and legend
ax.set_xlabel('Month')
ax.set_ylabel('Freight Volume (kg)')
ax.set_title('Freight Volume by Month')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Step 8: Set the grid lines
ax.grid(ls='dashed')

# Step 9: Automatically resize the image and save it
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-140159_4.png', bbox_inches='tight')

# Step 10: Clear the current image state
plt.clf()