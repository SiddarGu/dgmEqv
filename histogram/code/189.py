import pandas as pd
import matplotlib.pyplot as plt

# Transform the given data into three variables: data_labels, data, line_labels
data_labels = ['Ticket Price Range ($)', 'Number of Sports Events']
line_labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data = [42, 35, 27, 20, 15, 10, 5, 2, 1, 0]

# Create dataframe
df = pd.DataFrame(list(zip(line_labels, data)), columns=data_labels)

# Create figure before plotting
fig = plt.figure(figsize=(14, 8))

# Add a subplot for a horizontal bar plot
ax = fig.add_subplot(111)

# Plot horizontal bar graph
ax.barh(df['Ticket Price Range ($)'], df['Number of Sports Events'],
        color='skyblue', edgecolor='black')

# Set the title of the figure
ax.set_title('Pricing Trends at Sports and Entertainment Events')

# Set grid
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Rotate the x-axis labels if too long
ax.tick_params(axis='y', labelrotation=0, labelsize=10)

# Set tight layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/189.png'
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
