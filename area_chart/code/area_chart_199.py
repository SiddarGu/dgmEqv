
# Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Define the data
data = {"Category": ["California", "New York", "Texas", "Florida", "Illinois", "Pennsylvania", "Ohio", "Michigan", "Tennessee", "Georgia", "Arizona"],
        "Baseball (Fans)": [500, 400, 300, 400, 200, 400, 300, 200, 400, 300, 200],
        "Basketball (Fans)": [400, 500, 400, 500, 300, 500, 400, 300, 500, 400, 300],
        "Soccer (Fans)": [600, 300, 500, 300, 400, 300, 500, 400, 300, 500, 400],
        "Football (Fans)": [300, 200, 300, 400, 500, 200, 300, 400, 400, 300, 500],
        "Hockey (Fans)": [200, 400, 200, 300, 300, 400, 200, 300, 300, 200, 300]}

# Convert data into a pandas dataframe
df = pd.DataFrame(data)

# Convert first column to string type
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Calculate max total value
max_total_value = df.iloc[:, 1:].sum(axis=1).max()
# Round max total value up to the nearest multiple of 10, 100 or 1000
if max_total_value < 100:
    max_total_value = round(max_total_value / 10) * 10
elif max_total_value < 1000:
    max_total_value = round(max_total_value / 100) * 100
else:
    max_total_value = round(max_total_value / 1000) * 1000

# Create a figure and axes
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the data with an area chart
ax.stackplot(df["Category"], df["Baseball (Fans)"], df["Basketball (Fans)"], df["Soccer (Fans)"], df["Football (Fans)"], df["Hockey (Fans)"], labels=["Baseball", "Basketball", "Soccer", "Football", "Hockey"], colors=["#FFA07A", "#7FFFD4", "#FFDAB9", "#87CEEB", "#DA70D6"], alpha=0.75)

# Set x and y limits
ax.set_xlim(0, len(df.index) - 1)
ax.set_ylim(0, max_total_value)

# Set y ticks
yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
ax.set_yticks(yticks)

# Set y tick labels
yticklabels = ["{:,.0f}".format(tick) for tick in yticks]
ax.set_yticklabels(yticklabels, fontsize=12)

# Set x tick labels
ax.set_xticklabels(df["Category"], fontsize=12, rotation=45, ha="right", rotation_mode="anchor")

# Set grid lines
ax.grid(color="#D3D3D3", linestyle="--")

# Set legend
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=5, fontsize=12)

# Set title
ax.set_title("Fan Distribution by State and Sport", fontsize=16)

# Automatically resize image
fig.tight_layout()

# Save the figure
fig.savefig("output/final/area_chart/png/20231228-145339_34.png", bbox_inches="tight")

# Clear the current image state
plt.clf()