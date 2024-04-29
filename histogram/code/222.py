import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    "Hotel Star Rating": ["1-star", "2-star", "3-star", "4-star", "5-star"],
    "Number of Bookings (Thousands)": [6, 12, 25, 20, 10]
}

# Transform data into variables
data_labels = ["Hotel Star Rating", "Number of Bookings (Thousands)"]
line_labels = data["Hotel Star Rating"]
data_values = data["Number of Bookings (Thousands)"]

# Create a pandas DataFrame
df = pd.DataFrame(list(zip(line_labels, data_values)), columns=data_labels)

# Set figsize to a larger setting to prevent content cut-off
plt.figure(figsize=(10, 6))

# Create bar chart
ax = plt.subplot()
df.plot(kind='bar', x='Hotel Star Rating', y='Number of Bookings (Thousands)',
        ax=ax, grid=True, rot=0, legend=False, color='skyblue')

# Setting the title and labels
plt.title('Hotel Bookings by Star Rating Category', fontsize=14)
plt.xlabel('Hotel Star Rating', fontsize=12)
plt.ylabel('Number of Bookings (Thousands)', fontsize=12)

# Rotate x-axis labels if needed
plt.xticks(rotation=45)

# Adjust layout to make sure everything fits
plt.tight_layout()

# Save the figure
output_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/222.png'
plt.savefig(output_path)

# Clear the current figure state
plt.clf()
