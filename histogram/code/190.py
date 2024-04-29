import matplotlib.pyplot as plt
import pandas as pd

# Data preparation
data_labels = ['Tons Transported (million)']
line_labels = ['Rail', 'Trucking', 'Air', 'Shipping', 'Pipeline']
data = [350, 525, 75, 250, 490]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Create the histogram
df.plot(kind='bar', ax=ax, rot=30, legend=False)

# Styling
ax.set_title("US Freight Transport Volume by Mode", fontsize=16)
ax.set_xlabel("Freight Type", fontsize=14)
ax.set_ylabel("Tons Transported (million)", fontsize=14)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Automatically adjust subplot params to give specified padding
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/190.png', format='png', dpi=300)

# Clear the current image state
plt.clf()
