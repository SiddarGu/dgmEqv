import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_strings = [
    "Government Expenditure ($ Billion),Sector",
    "1200-1300,Defense",
    "900-1000,Social Security",
    "700-800,Healthcare",
    "500-600,Education",
    "300-400,Infrastructure",
    "200-300,Veterans Benefits",
    "100-200,Energy and Environment",
    "50-100,Science and Technology",
    "0-50,Agriculture"
]

# Extracting data_labels, line_labels, and data
data_labels = ['Expenditure ($ Billion)']
line_labels = []
data = []

for item in data_strings[1:]:  # Skip the header
    expenditure_range, sector = item.split(',')
    avg_expenditure = sum(map(int, expenditure_range.split('-'))) / 2
    line_labels.append(sector)
    data.append(avg_expenditure)

# Create a DataFrame
df = pd.DataFrame(list(zip(data)), index=line_labels, columns=data_labels)

# Create the figure and axis
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Plot and format the histogram
df.plot(kind='bar', ax=ax, legend=False, grid=True, color='skyblue')

# Set title and labels
ax.set_title('U.S. Government Budget Allocation by Sector (2023)', fontweight='bold')
ax.set_ylabel('Expenditure ($ Billion)', fontweight='bold')
ax.set_xlabel('Sector', fontweight='bold')

# Rotate x labels and wrap text for better visibility
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', wrap=True)

# Automatically adjust subplot params for the figure to fit into the window
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/161.png'
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
