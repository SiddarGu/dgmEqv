import matplotlib.pyplot as plt
import squarify

# Parsing the data into variables
data_labels = ["Usage Share (%)"]
line_labels = ["Social Media", "Online Shopping", "Streaming Services", "Cloud Computing", 
               "Online Gaming", "E-Learning", "Remote Work", "Cybersecurity"]
data = [25, 20, 18, 12, 10, 7, 5, 3]

# Creating and customizing the treemap
plt.figure(figsize=(12, 8))  # Set a larger figure size
squarify.plot(sizes=data, label=line_labels, alpha=0.7, pad=True, text_kwargs={'wrap': True})

# Style the plot
plt.title("Proportional Usage of Internet Services and Technologies", fontsize=14)
plt.axis('off')  # Hide the axes
plt.tight_layout()  # Automatically resize the figure

# Saving the figure to the specified path
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/33.png"
plt.savefig(save_path, format='png')

# Clear the current figure state
plt.clf()
