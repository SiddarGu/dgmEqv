import matplotlib.pyplot as plt
import squarify

# Preparing the data
data_labels = ["Health and Human Services", "National Defense", "Education", 
               "Social Security", "Infrastructure", "Environmental Protection", 
               "Law Enforcement", "Science and Technology", "Agriculture"]
data = [25, 20, 15, 15, 10, 5, 5, 3, 2]
line_labels = [f"{label} ({value}%)" for label, value in zip(data_labels, data)]

# Setting up colors
cmap = plt.cm.Blues
mini = min(data)
maxi = max(data)
norm = plt.Normalize(vmin=mini, vmax=maxi)
colors = [cmap(norm(value)) for value in data]

# Creating the figure and plotting the treemap
plt.figure(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, color=colors, alpha=0.7, text_kwargs={'wrap': True})

# Adding title to the treemap
plt.title("Allocation of Government Budget by Policy Area in 2023", fontsize=14)

# Removing axes
plt.axis('off')

# Adjust layout to prevent content from being cut off and to resize the figure
plt.tight_layout()

# Saving the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1050.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure after saving
plt.clf()
