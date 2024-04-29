import pandas as pd
import matplotlib.pyplot as plt

# Data preparation
data_labels = ['Incidents Reported']
line_labels = ['Violent Crimes', 'Property Crimes', 'Drug Offenses', 'Fraud',
               'Public Order Offenses', 'Cyber Crimes', 'Environmental Crimes', 'Other Offenses']
data = [350, 750, 550, 170, 460, 110, 65, 290]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Create a figure and a subplot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot()

# Plotting the horizontal bar chart
df.plot(kind='barh', ax=ax, legend=False)

# Adding grid, title and formatting
plt.title('Annual Incidents Reported by Crime Type')
plt.grid(True)

# Handle long labels
ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha='right', fontsize=9, wrap=True)

# Automatically adjust subplot params for the figure
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/36.png', format='png', dpi=300)

# Clear the current figure's state
plt.clf()
