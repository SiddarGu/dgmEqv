import matplotlib.pyplot as plt
import seaborn as sns

# Given data
data_labels = ["Sales Volume (Million)"]
line_labels = ["Packaged Foods", "Beverages", "Confectionery", 
               "Dairy Products", "Meat and Poultry", "Seafood", 
               "Fruits and Vegetables", "Baked Goods", "Specialty Foods"]
data = [35.2, 42.8, 19.5, 27.3, 23.7, 16.4, 31.9, 24.1, 17.6]

# Creating the figure and adding subplots
plt.figure(figsize=(12, 8))
ax = plt.subplot()

# Creating histogram
sns.barplot(x=line_labels, y=data, palette='viridis')

# Adjusting the appearance
ax.set_title('Sales Performance per Product Category in the Food and Beverage Industry')
ax.set_ylabel(data_labels[0])
plt.xticks(rotation=45, ha='right', wrap=True)

# Enhancing layout and aesthetics
plt.grid(axis='y')
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/52.png'
plt.savefig(save_path, format='png')

# Clearing the current figure state to prevent overlap with any future plots
plt.clf()
