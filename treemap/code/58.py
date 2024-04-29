import matplotlib.pyplot as plt
import squarify

# Data
data_labels = ["Banking", "Investment", "Insurance", "Real Estate", "Consumer Goods", "Technology", "Healthcare", "Energy", "Manufacturing"]
data = [22, 18, 15, 14, 9, 8, 7, 4, 3]
line_labels = ["Revenue Share (%)"]

# Treemap Plot
plt.figure(figsize=(12, 8))  # Larger size for clarity
colors = plt.cm.tab20c.colors  # Using the 'tab20c' colormap for variety

# Creating a squarified treemap
squarify.plot(
    sizes=data,
    label=data_labels,
    color=colors,
    alpha=0.7,
    text_kwargs={'fontsize':12, 'wrap':True}
)

plt.title('Revenue Distribution across Business and Finance Sectors', fontsize=16)

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1003.png', dpi=100)  # Save with clear resolution

# Clear the current image state
plt.clf()
