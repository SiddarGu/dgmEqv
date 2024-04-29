import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Parsing the given data into variables
data_labels = ["Housing Price Range (Thousands)", "Number of Sales"]
line_labels = ["<100", "100-200", "200-300", "300-400", "400-500", "500-600", "600-700", 
               "700-800", "800-900", "900-1000"]
data = [20, 35, 50, 45, 30, 20, 15, 10, 8, 5]

# Creating a DataFrame
df = pd.DataFrame(data, index=line_labels, columns=[data_labels[1]])

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Creating a figure with a larger figsize
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Create a vertical histogram (bar plot in seaborn)
barplot = sns.barplot(x=df.index, y=df["Number of Sales"], palette="viridis", ax=ax)

# Setting the title of the figure
ax.set_title('Home Sales Distribution by Price Range', fontsize=16)

# Rotating the x labels if they are too long
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")

# Adjust the layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/196.png'

# Create necessary directories if not exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Save the figure
plt.savefig(save_path)

# Clear the current image state
plt.clf()
