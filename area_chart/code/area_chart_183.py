
# Importing necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Creating a dictionary of data
data = {'Category': ['Residential', 'Commercial', 'Industrial', 'Agricultural', 'Transportation', 'Waste Management', 'Government', 'Education', 'Healthcare', 'Construction'],
        'Electricity Consumption (kWh)': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000],
        'Water Usage (gallons)': [8000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000],
        'Recycling (lbs)': [1000, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]}

# Converting dictionary to pandas DataFrame
df = pd.DataFrame(data)

# Converting first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Setting figure size
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting area chart
ax.stackplot(df['Category'], df['Electricity Consumption (kWh)'], df['Water Usage (gallons)'], df['Recycling (lbs)'],
             labels=['Electricity Consumption (kWh)', 'Water Usage (gallons)', 'Recycling (lbs)'],
             colors=['#99ccff', '#ffcc99', '#99ff99'], alpha=0.7)

# Setting ticks and tick labels for x-axis
ax.set_xticks(range(len(df.index)))
ax.set_xticklabels(df['Category'], rotation=45, ha='right', rotation_mode='anchor')

# Setting y-axis limit and ticks
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
max_total_value = np.ceil(max_total_value / 100) * 100  # Rounding up to nearest multiple of 100
ax.set_ylim(0, max_total_value)
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Adding grid lines
ax.grid(which='major', axis='both', linestyle='--', alpha=0.5)

# Setting legend outside the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# Setting title and labels
ax.set_title('Environmental Impact by Industry Category')
ax.set_xlabel('Category')
ax.set_ylabel('Amount')

# Automatically resizing and saving the image
plt.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_14.png', bbox_inches='tight')

# Clearing current image state
plt.clf()

# Printing success message
print("Chart generated successfully!")