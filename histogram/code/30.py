import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Define the data
data_labels = ['Number of Users (Million)']
line_labels = ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9']
data = [
    35,
    50,
    70,
    65,
    40,
    20,
    10,
    5,
    2
]

# Create a DataFrame
df = pd.DataFrame(data, columns=data_labels, index=line_labels)
df.index.name = 'Average Daily Use (Hours)'

# Create a Figure and a subplot
plt.figure(figsize=(10, 8))
ax = plt.subplot()

# Seaborn histogram
sns.barplot(data=df.reset_index(), x='Average Daily Use (Hours)', y='Number of Users (Million)', ax=ax)

# Rotate the labels if necessary
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", wrap=True)

# Enhancing the design with grids
plt.grid(True)

# Set the title of the figure
plt.title('Global Social Media Usage by Average Daily Time Spent')

# Automatically resize the image
plt.tight_layout()

# Define the save path
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/histogram/png/30.png'

# Create directories if not exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path)

# Clear the current image state
plt.clf()
