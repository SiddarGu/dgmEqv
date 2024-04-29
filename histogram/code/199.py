import matplotlib.pyplot as plt
import seaborn as sns

# Preparing the data
data_labels = ['Annual Sales ($ Billion)']
line_labels = ['Snacks', 'Beverages', 'Packaged Foods', 'Fresh Produce', 'Dairy Products', 'Meat and Poultry', 'Seafood', 'Confectionery', 'Bakery Items']
data = [10.5, 20.3, 14.7, 9.2, 13.5, 15.8, 7.6, 8.4, 12.9]

# Creating a DataFrame for Seaborn
import pandas as pd
df = pd.DataFrame(data, index=line_labels, columns=data_labels)

# Setting up the plot
plt.figure(figsize=(10, 6))
ax = plt.subplot()

# Creating the histogram
sns.barplot(data=df, x=df.index, y='Annual Sales ($ Billion)', ax=ax, palette="viridis")

# Setting up the title and labels
ax.set_title('Annual Sales Distribution Across Food and Beverage Product Categories', fontsize=15)
plt.xticks(rotation=30, ha='right')  # Rotate the labels to ensure they fit and are readable
plt.xlabel('Product Category')
plt.ylabel('Annual Sales ($ Billion)')

# Customizing the design
sns.despine(bottom=True)
plt.grid(axis='y', linestyle='--', linewidth=0.7, alpha=0.7)
ax.tick_params(axis='both', which='both', length=0)

# Automatically adjusts subplot params so the subplot(s) fits into the figure area
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/199.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state
plt.clf()
