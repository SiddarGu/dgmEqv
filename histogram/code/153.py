import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_labels = ['Number of Donations']
line_labels = ['<50', '50-100', '100-200', '200-500', '500-1000', '1000-5000', '5000-10000', '>10000']
data = [120, 90, 75, 60, 35, 25, 10, 5]

# Create DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Set the figsize larger to prevent content from being obscured
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create horizontal bar plot
df['Number of Donations'].plot(kind='barh', legend=False, ax=ax)

# Customize the plot to make it fancy
ax.set_title('Distribution of Donation Sizes to Charities and Nonprofits')
ax.set_xlabel('Donation Size ($)')
ax.set_ylabel('Number of Donations')

# Enable grid for better readability
ax.grid(True, linestyle='--', which='major', color='grey', alpha=.25)

# Rotate or wrap labels if needed
ax.set_yticklabels(df.index, rotation=30)
plt.xticks(rotation=30)

# Set a tight layout to automatically adjust subplot params so that the subplot(s) fits in to the figure area
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/153.png')

# Clear the current figure to prevent overlap of previous plots in future plots
plt.clf()
