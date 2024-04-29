import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data_labels = ['Donation Size ($)', 'Number of Donations']
line_labels = [
    '1-100', '100-500', '500-1000', '1000-5000', 
    '5000-10000', '10000-50000', '50000-100000', '100000-500000'
]
data = [
    150, 120, 80, 60,
    30, 20, 10, 5
]

# Creating a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Plotting the histogram
plt.figure(figsize=(10, 8))
ax = plt.subplot()

df.plot(kind='bar', ax=ax, rot=0, legend=False, color='skyblue', edgecolor='black')

# Set the title and labels
ax.set_title('Donation Size Distribution to Charities and Nonprofits')
ax.set_xlabel('Donation Size ($)')
ax.set_ylabel('Number of Donations')
plt.xticks(rotation=45, ha='right')  # Rotate x labels to show them better

# Add grid and style
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.box(False)
plt.tight_layout()

# Save the image
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/132.png', format='png')

# Clear the current figure state
plt.clf()
