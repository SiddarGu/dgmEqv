import pandas as pd
import matplotlib.pyplot as plt
import os

# Data
data_labels = ['Electricity Generation (TWh)']
line_labels = ['Coal', 'Natural Gas', 'Nuclear', 'Hydroelectric', 'Wind', 'Solar', 'Biomass', 'Geothermal']
data = [2401.5, 4002.2, 2455.8, 1232.0, 1820.1, 1134.4, 500.5, 92.3]

# Create a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Plot settings
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)

# Create horizontal bar plot
df.plot(kind='barh', ax=ax, legend=False)

# Set title and labels
ax.set_title('Electricity Generation by Energy Source in the United States')
ax.set_xlabel('Electricity Generation (TWh)')

# Grid, tight layout and rotation for long labels
ax.grid(True)
plt.tight_layout()

# Saving the figure to the specified path
output_dir = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png'
output_file = '59.png'
output_path = os.path.join(output_dir, output_file)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

plt.savefig(output_path)

# Clear the current figure state after saving
plt.clf()
