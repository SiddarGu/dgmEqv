
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data
data = {"Sector": ["Agriculture", "Transportation", "Manufacturing", "Retail", "Hospitality", "Healthcare", "Education", "Construction", "Government", "Energy"], 
        "Water Usage (mL)": [2000, 1500, 1000, 500, 1000, 500, 100, 500, 500, 1500], 
        "Energy Consumption (kWh)": [500, 3000, 4000, 2000, 3000, 1500, 500, 2000, 1000, 3000], 
        "Carbon Footprint (kg)": [1000, 5000, 3000, 1000, 2000, 500, 200, 1000, 500, 2000], 
        "Waste Production (kg)": [1500, 1000, 2000, 500, 1000, 500, 100, 500, 500, 500]}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value for y axis
max_total_value = df.iloc[:, 1:].sum(axis=1).max() # Get max total value
max_total_value = np.ceil(max_total_value / 1000) * 1000 # Round up to nearest multiple of 1000
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32) # Generate y ticks
yticklabels = ["{}k".format(int(y/1000)) for y in yticks] # Generate y tick labels

# Set figure size and create axes
fig, ax = plt.subplots(figsize=(10, 6))

# Stack plot
ax.stackplot(df.index, df.iloc[:, 1:].T, labels=df.columns[1:], colors=["#C2E3FF", "#99CCFF", "#6688FF", "#3366FF"]) # Plot data with area chart

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1) # Set x limit
ax.set_ylim(0, max_total_value) # Set y limit

# Set ticks and tick labels
ax.set_xticks(df.index) # Set x ticks
ax.set_xticklabels(df.iloc[:, 0], rotation=45, ha="right", rotation_mode="anchor", wrap=True) # Set x tick labels with rotation and wrapping
ax.set_yticks(yticks) # Set y ticks
ax.set_yticklabels(yticklabels) # Set y tick labels

# Set grid lines
ax.grid(color="grey", linestyle="dotted") # Set background grid lines

# Set legend
ax.legend(loc="upper left", bbox_to_anchor=(1, 1)) # Set legend position

# Set labels and title
ax.set_xlabel("Sector") # Set x label
ax.set_ylabel("Total Resource Consumption") # Set y label
ax.set_title("Resource Consumption and Environmental Impact by Sector") # Set title

# Automatically resize image
fig.tight_layout()

# Save figure
fig.savefig("output/final/area_chart/png/20231228-155112_12.png", bbox_inches="tight")