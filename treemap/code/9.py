import matplotlib.pyplot as plt
import squarify

# Given data
categories_with_percentages = [
    ("Social Networking", 30),
    ("Online Shopping", 20),
    ("Content Streaming", 25),
    ("Search Engines", 10),
    ("Online Gaming", 5),
    ("Email", 5),
    ("Blogs and Forums", 3),
    ("Web Development", 2)
]

# Transforming the given data
data_labels = [item[0] for item in categories_with_percentages]  # Extracting category labels
data = [item[1] for item in categories_with_percentages]  # Extracting percentages

# Set up figure size
fig, ax = plt.subplots(figsize=(12, 8))

# Using squarify to plot a treemap
squarify.plot(sizes=data, label=data_labels, color=None, alpha=0.6, text_kwargs={'wrap': True})

# Set title and adjust layout
plt.title('Web Usage Distribution: Social Media and Internet Activities')
plt.axis('off')
plt.tight_layout()

# Save figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/9.png'
plt.savefig(save_path, format='png', dpi=300)

# Clear the current figure's state to avoid any plot overlapping issues
plt.clf()
