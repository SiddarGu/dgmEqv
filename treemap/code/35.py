import matplotlib.pyplot as plt
import squarify

# Given data transformation into three variables.
data_labels = ["K-12", "Higher Education", "Early Childhood Education", "Continuing Education", "Educational Technology", "Research and Development"]
data = [40, 25, 15, 10, 5, 5]
line_labels = ["Spending (%)"]

# Drawing the treemap.
plt.figure(figsize=(12, 8))
colors = plt.cm.viridis([0.6, 0.5, 0.4, 0.3, 0.2, 0.1])
squarify.plot(
    sizes=data,
    label=[f"{label}\n({pct}%)" for label, pct in zip(data_labels, data)],
    color=colors,
    alpha=0.8,
    edgecolor="white",
    linewidth=3,
    text_kwargs={'wrap': True}
)
plt.title("Percentage of Educational Spending by Level", fontsize=18)
plt.axis('off')

# Automatically resize the image, then save and clear the image state.
plt.tight_layout()
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/35.png"
plt.savefig(save_path, format='png', dpi=300)
plt.clf()
