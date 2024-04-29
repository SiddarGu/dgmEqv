import matplotlib.pyplot as plt
import squarify

# Given data
data_list = [
    ["Anthropology", 18],
    ["Sociology", 16],
    ["Psychology", 15],
    ["History", 14],
    ["Linguistics", 12],
    ["Philosophy", 10],
    ["Economics", 9],
    ["Political Science", 6],
]

# Transform data into required variables
data_labels = [row[0] for row in data_list]
data = [row[1] for row in data_list]
line_labels = ["Research Funding (%)"]

# Plot treemap using squarify
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=data, label=data_labels, alpha=0.8, text_kwargs={'wrap': True})
plt.title('Allocation of Research Funding in Social Sciences and Humanities', fontsize=18)

# Resize the image properly before saving
plt.tight_layout()

# Save the figure to the given path; ensure the directory exists before running this code.
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/treemap/png/1023.png'
plt.savefig(save_path)
plt.close()
