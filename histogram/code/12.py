import pandas as pd
import matplotlib.pyplot as plt

# Define the data
data_labels = ['Disease Incidence Rate (per 1000)', 'Number of Cases']
line_labels = ['Heart Disease', 'Influenza', 'Diabetes', 'Asthma', 'Cancer', 'Stroke', 'Arthritis', 'Hypertension']
data = [7.2, 13.5, 8.9, 9.4, 5.7, 4.3, 11.8, 12.1]

# Convert the data into a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=['Number of Cases'])

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Create the histogram
df['Number of Cases'].plot(kind='bar', ax=ax, color='skyblue')

# Set the title and labels
ax.set_title('Prevalence of Common Diseases in the Population', fontsize=14)
ax.set_xlabel('Diseases', fontsize=12)
ax.set_ylabel('Incidence Rate (per 1000)', fontsize=12)

# Add grid
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Rotate the x-axis labels if they are too long
ax.tick_params(axis='x', rotation=45)

# Automatically adjust subplot params
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/12.png', dpi=300)

# Clear the current figure state
plt.clf()
