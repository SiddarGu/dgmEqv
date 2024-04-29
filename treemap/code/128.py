import matplotlib.pyplot as plt
import squarify

# Given data
data_labels = ['Category', 'Sales Share (%)']
line_labels = ['Clothing and Apparel', 'Electronics', 'Home Furnishings', 'Books and Media', 'Groceries', 'Health and Beauty', 'Toys and Hobbies']
data = [35, 25, 15, 10, 8, 4, 3]

# Plotting a treemap
plt.figure(figsize=(12, 8))  # Setting the figure size
colors = plt.cm.Paired(range(len(data)))  # Defining colors for each section

# Adding padding around each rectangle by specifying a value for the pad argument. Here as an example, pad=4
squarify.plot(sizes=data, label=line_labels, alpha=0.8, color=colors, pad=4) 

# The title of the figure
plt.title('E-commerce Sales Distribution Across Retail Categories in 2023', fontsize=18)

# Prevent content from being displayed improperly
plt.axis('off')  # Turn off the axis
plt.tight_layout()  # Automatically resize the image

# Saving the figure to the specified path
plt.savefig('/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/128.png', format='png', dpi=300)  # Note: Ensure this path exists

# Clear the current image state
plt.clf()
plt.close()
