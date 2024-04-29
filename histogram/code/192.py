import matplotlib.pyplot as plt
import os

# Given data
data_labels = ['Crop Yield (tons/hectare)', 'Number of Farms']
line_labels = ['Wheat', 'Rice', 'Maize', 'Barley', 'Soybean', 'Potato', 'Tomato', 'Lettuce', 'Carrot']
data = [3.2, 4.1, 5.7, 2.8, 3.5, 10.2, 8.4, 7.1, 6.5]

# Plotting
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(line_labels, data, color=plt.cm.Paired.colors)
ax.set_title('Agriculture Productivity: Yield Per Hectare Across Various Farms')
ax.set_xlabel(data_labels[0])
ax.set_ylabel(data_labels[1])
ax.grid(True)

# Rotate labels if they are too long
plt.yticks(wrap=True)
# Automatically adjust subplot params so the subplot(s) fits into the figure area
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/192.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure's state
plt.clf()
