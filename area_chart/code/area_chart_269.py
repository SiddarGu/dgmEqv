
# Import necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dictionary with data
data = {'Category': ['Physics', 'Chemistry', 'Computer Science', 'Biology', 'Mathematics'],
        'United States': [20000, 18000, 25000, 22000, 15000],
        'China': [18000, 23000, 20000, 25000, 16000],
        'Japan': [15000, 20000, 22000, 18000, 23000],
        'Germany': [25000, 22000, 24000, 23000, 20000],
        'United Kingdom': [22000, 18000, 22000, 21000, 17000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Create area chart
fig, ax = plt.subplots(figsize=(12, 8)) # Set figure size
ax.stackplot(df.iloc[:, 0], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd'], alpha=0.8) # Plot data with stacked area chart
ax.set_title("Distribution of Scientists in Various Fields and Countries") # Set title
ax.set_xlabel("Category") # Set x label
ax.set_ylabel("Number of Scientists") # Set y label
ax.legend(loc='upper left', bbox_to_anchor=(1, 1)) # Set legend position
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5) # Add grid lines
ax.set_xlim(0, len(df.index) - 1) # Set x axis limits
max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Calculate max total value
max_total_value = np.ceil(max_total_value / 1000) * 1000 # Round up to nearest multiple of 1000
ax.set_ylim(0, max_total_value) # Set y axis limits
ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)) # Set y axis ticks
fig.tight_layout() # Automatically resize image
plt.savefig('output/final/area_chart/png/20231228-155112_3.png', bbox_inches='tight') # Save figure
plt.show() # Display figure
plt.close() # Clear current image state