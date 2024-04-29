import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_str = """Profit Range ($Million),Number of Companies
0-50,18
50-100,22
100-150,20
150-200,15
200-250,10
250-300,8
300-350,5
350-400,2
400-450,1
450-500,1"""

# Transforming the data into a DataFrame
data = pd.DataFrame([x.split(',') for x in data_str.split('\n')])
data.columns = data.iloc[0]
data = data[1:]
data['Number of Companies'] = pd.to_numeric(data['Number of Companies'])
data_labels = data.columns[1:]
line_labels = data['Profit Range ($Million)']

# Create figure and subplot for horizontal histogram
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# Plot horizontal bar chart
ax.barh(line_labels, data['Number of Companies'].values, color=plt.cm.viridis(data['Number of Companies'].values / data['Number of Companies'].max()))

# Setting the title of the figure
ax.set_title('Corporate Profit Distribution Across Various Ranges')

# Set the grid
ax.grid(which='both', linestyle='--', linewidth=0.5)

# Rotate x tick labels if too long
plt.xticks(rotation=45, ha='right')
plt.yticks(wrap=True)

# Resize the image before saving
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/57.png'
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
