import pandas as pd
import matplotlib.pyplot as plt

# Data processing
data_labels = ['Average Daily Caloric Intake (kcal)', 'Percentage of Population (%)']
line_labels = ['1500-2000', '2000-2500', '2500-3000', '3000-3500', '3500-4000', '4000-4500', '4500-5000', '5000-5500']
data = [15, 30, 25, 20, 10, 5, 3, 2]

# Convert to DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create a horizontal bar plot
df.plot(kind='barh', y=data_labels[1], x=data_labels[0], ax=ax, color='skyblue', edgecolor='black')

# Setting the title
plt.title('Distribution of Daily Caloric Intake among Adults')

# Adjusting the x-axis labels to avoid overlap
plt.xticks(rotation=45)
plt.xlabel(data_labels[1])
plt.ylabel(data_labels[0])

# Adding grid
plt.grid(True)

# To wrap the labels if they're too long
ax.set_yticklabels(line_labels, wrap=True)

# Make sure the layout fits well and save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/29.png')

# Clear the current figure state
plt.clf()
