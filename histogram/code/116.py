import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Provided data
data = [
    [120000, 95000, 70000, 50000, 30000, 25000, 18000, 12000],
]
data_labels = [
    'Letters and Documents',
    'Clothing and Apparel',
    'Electronics',
    'Pharmaceuticals',
    'Furniture',
    'Perishables',
    'Industrial Equipment',
    'Hazardous Materials'
]
line_labels = ['Average Daily Deliveries']

# Creating a DataFrame
df = pd.DataFrame(data, columns=data_labels, index=line_labels)

# Initialize a matplotlib figure with a larger size
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Plotting the horizontal histogram
sns.barplot(data=df, orient='h', ax=ax)

# Customizing the plot
ax.set_title('Average Daily Deliveries by Cargo Type in the Logistics Industry')
ax.set_xlabel('Average Daily Deliveries')
ax.set_ylabel('Cargo Type')
plt.xticks(rotation=45)
plt.yticks(fontsize=9, wrap=True)
ax.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust the layout to make sure everything fits without overlapping
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/116.png'
# Before saving, check if directory exists, if not, create it
os.makedirs(os.path.dirname(save_path), exist_ok=True)
plt.savefig(save_path)

# Clear the current figure's state to prevent overlap with future plots
plt.clf()
