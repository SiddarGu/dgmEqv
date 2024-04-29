import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_str = """Product,Defect Rate (%),Units Produced (Thousands)
Electrical Components,0.5,320
Consumer Electronics,0.75,289
Automotive Parts,0.6,415
Textiles,0.25,540
Pharmaceuticals,0.4,150
Food and Beverages,0.3,670"""

# Transform data string into pandas DataFrame
data = pd.DataFrame([x.split(',') for x in data_str.split('\n')])
data.columns = data.iloc[0]
data = data[1:]
data = data.set_index('Product')
data.index.name = None
data = data.astype(float)

# Extract variables
data_labels = data.columns.tolist()
line_labels = data.index.tolist()

# Create a figure with larger figsize
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Plot vertical histogram using pandas
data["Defect Rate (%)"].plot(kind='bar', color='skyblue', ax=ax)

# Title and labels
plt.title('Product Defect Rates Across Manufacturing Industries')
plt.xlabel('Product')
plt.ylabel('Defect Rate (%)')

# Set the rotation of xtick labels if they are too long
plt.xticks(rotation=45, ha='right', wrap=True)

# Enhancing the plot with grid, larger font size, and tight layout for better fit
plt.grid(True, linestyle='--', alpha=0.7)
plt.gca().tick_params(axis='both', which='major', labelsize=12)
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/23.png')

# Clear the current figure state to prevent overlap in future plots
plt.clf()
