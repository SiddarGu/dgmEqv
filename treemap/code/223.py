import matplotlib.pyplot as plt
import squarify

# Extracted data
data_labels = ['Natural Gas', 'Coal', 'Nuclear', 'Renewables', 'Petroleum', 'Hydroelectric']
data = [25, 22, 19, 17, 12, 5]
line_labels = ["Utility Usage (%)"]

# Map the data to squares
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, aspect="auto")
squarify.plot(sizes=data, label=data_labels, color=None, alpha=0.6)

# Title and settings
plt.title('Utility Usage Breakdown by Energy Source', fontsize=15)
plt.axis('off')

# Adjust text labels
for label in ax.texts:
    text = label.get_text()
    if len(text) > 10:
        label.set_text(text[:10] + '...')

# Resize layout to fit and prevent content from being cut off
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/chart_simulation_final/treemap/png/223.png'
plt.savefig(save_path, format='png', dpi=300)
plt.close()  # Clear the current figure to prevent memory issues if this code runs in a loop
