import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Define the data
data_string = """Crop Type,Yield (tons per hectare)
Wheat,3.2
Corn,5.8
Rice,4.1
Barley,2.7
Soybeans,2.9
Potatoes,15.0
Cotton,1.4
Sugarcane,70.0"""

# Split the string into lines
data_lines = data_string.split('\n')

# Extract data labels and data
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data = [float(line.split(',')[1]) for line in data_lines[1:]]

# Create a DataFrame
df = pd.DataFrame(list(zip(line_labels, data)), columns=['Crop Type', 'Yield'])

# Setting up the plot
plt.figure(figsize=(10, 8))
ax = plt.subplot(111)

# Create the histogram
sns.barplot(x='Crop Type', y='Yield', data=df, ax=ax, palette='viridis')

# Beautifying the plot
ax.set_title('Yield of Various Crops per Hectare in Agriculture Production')
ax.set_xlabel('Crop Type')
ax.set_ylabel('Yield (tons per hectare)')
plt.xticks(rotation=45, wrap=True)

# Apply tight layout and save the figure
plt.tight_layout()
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/51.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the plot
plt.clf()
