import matplotlib.pyplot as plt
import pandas as pd

# Define the data
data_labels = ['Average Yearly Revenue ($Million)', 'Number of Companies']
line_labels = [
    'Less than 1', '1-5', '5-10', '10-20', 
    '20-50', '50-100', '100-200', '200-300', 
    '300-500', '500+'
]
data = [12, 25, 30, 22, 19, 10, 6, 4, 2, 1]  # Number of companies


# Create a DataFrame
df = pd.DataFrame(data=data, columns=[data_labels[1]], index=line_labels)
df.index.name = data_labels[0]

df = df.transpose()

# Create a figure and a set of subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Create horizontal bar plot
df.plot(kind='barh', ax=ax, legend=True)

# Set labels and title
ax.set_xlabel('Number of Companies')
ax.set_ylabel('Average Yearly Revenue ($Million)')
ax.set_title('Financial Performance of Food and Beverage Companies')

# Set grid
ax.grid(True)

# # Rotate the y tick labels to show clearly if they are too long
# for tick in ax.get_yticklabels():
#     tick.set_rotation(45)
#     tick.set_wrap(True)  # Wrap the label text
ax.set_yticks([])

# Set layout to be tight
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/96.png')

# Clear current figure state
plt.clf()
