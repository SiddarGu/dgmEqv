import matplotlib.pyplot as plt
import squarify

# Given data in a structured format
data = [
    ["Education Sector", "Spending Allocation (%)"],
    ["Higher Education", 30],
    ["Primary Education", 25],
    ["Secondary Education", 20],
    ["Vocational Training", 10],
    ["Special Education", 8],
    ["Educational Technology", 4],
    ["Research and Development", 3]
]

# Transform the given data
data_labels = data[0][1:]  # ["Spending Allocation (%)"]
line_labels = [row[0] for row in data[1:]]  # Academic sectors
values = [row[1] for row in data[1:]]  # Corresponding values

# Plotting
fig = plt.figure(figsize=(12, 8))
squarify.plot(sizes=values, label=line_labels, value=values, alpha=.8)
plt.title("Allocation of Educational Spending Across Various Academic Sectors")

# Rotate labels if needed (optional)
plt.xticks([]) 
plt.yticks([])

# Wrap labels if necessary
# plt.gca().set_xticklabels(None, wrap=True)

# Adjust layout to prevent content from being clipped
plt.tight_layout()

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/39.png"
plt.savefig(save_path)

# Clear the current figure state
plt.clf()
