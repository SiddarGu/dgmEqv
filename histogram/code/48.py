import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Data preparation
data_labels = ['Unit Production Cost (USD)']
line_labels = ['Raw Materials', 'Assembly', 'Quality Control', 'Packaging', 'Storage', 'Distribution']
data = [5.2, 3.8, 2.5, 1.2, 0.6, 0.75]

# Creating a DataFrame from the provided data
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Setting the plot style
sns.set_style("whitegrid")

# Creating a larger figure to prevent content from being displayed scrunched together
plt.figure(figsize=(10, 8))

# Adding a subplot to the current figure
ax = plt.subplot()

# Plotting a horizontal bar plot using seaborn
sns.barplot(x=data, y=line_labels, palette="viridis", ax=ax)

# Setting the title of the figure
ax.set_title('Unit Production Cost Breakdown Across Manufacturing Phases')

# If the text length of the label is too long, display label on separate lines
ax.set_yticklabels([label if len(label) <= 30 else '\n'.join(label.split()) for label in line_labels], rotation=0)

# Automatically resize the image
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/1001.png'
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path, format='png')

# Clear the current figure's state
plt.clf()
