
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Create dictionary
data = {"Year": [2016, 2017, 2018, 2019, 2020, 2021],
        "Healthcare (Spending)": [5000, 5500, 6000, 6500, 7000, 7500],
        "Education (Spending)": [6000, 6500, 7000, 7500, 8000, 8500],
        "Infrastructure (Spending)": [7000, 7500, 8000, 8500, 9000, 9500],
        "Social Programs (Spending)": [8000, 8500, 9000, 9500, 10000, 11000]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set axis labels
ax = fig.add_subplot(111)
ax.set_xlabel("Year")
ax.set_ylabel("Spending (in millions)")

# Set title
plt.title("Government Spending by Sector from 2016 to 2021")

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()

# Ceil max_total_value to nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = np.ceil(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = np.ceil(max_total_value / 100) * 100
else:
    max_total_value = np.ceil(max_total_value / 1000) * 1000

# Set y-axis ticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set x-axis range
ax.set_xlim(0, len(df.index) - 1)

# Set background grid lines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

# Plot data as stacked area chart
ax.stackplot(df["Year"], df["Healthcare (Spending)"], df["Education (Spending)"], 
             df["Infrastructure (Spending)"], df["Social Programs (Spending)"],
             colors=['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728'], alpha=0.8, labels=['Healthcare', 'Education', 'Infrastructure', 'Social Programs'])

# Set legend
ax.legend(loc='upper left')

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/area_chart/png/20231228-131755_52.png", bbox_inches='tight')

# Clear current image state
plt.clf()