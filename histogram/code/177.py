import pandas as pd
import matplotlib.pyplot as plt

# Provided data
data_labels = ["Yield (million metric tons)"]
line_labels = ["Maize", "Rice", "Wheat", "Soybean", "Potatoes", "Tomatoes", "Sugarcane", "Cotton", "Coffee"]
data = [81.2, 77.5, 73.8, 45.6, 36.1, 16.3, 159.4, 25.7, 10.8]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create figure and histogram
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plotting a horizontal bar chart
df.plot(kind='barh', legend=False, ax=ax, color='skyblue')

# Add grid, title, and labels
plt.grid(True, linestyle='--', alpha=0.7)
plt.title('Global Crop Yield Distribution in Agriculture Sector')
plt.xlabel(data_labels[0])

# Rotate x-axis labels if necessary
plt.xticks(rotation=45, ha='right')

# Layout adjustment to accommodate the longer labels and prevent content clipping
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/177.png')

# Clear the current figure state to avoid memory issues
plt.clf()
