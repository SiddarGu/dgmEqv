
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

data_labels = ["Quality Control", "Automation", "Development", "Raw Materials", "Logistics"] 
data = [23, 30, 17, 20, 10]
line_labels = ["Category", "ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# Plot data
ax.pie(data, startangle=90, counterclock=False, colors=['#00AEFF', '#FFD43B', '#2F4858', '#2F9DB5', '#FF3D3D'], wedgeprops={"edgecolor":"k",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True})

# Create white center circle
center_circle = Circle((0, 0), 0.70, fc='white')
ax.add_artist(center_circle)

# Set title
ax.set_title("Manufacturing and Production Output Overview - 2023", fontsize=14)

# Set legend
ax.legend(data_labels, loc="upper right")

# Configure axis
ax.axis('equal')
ax.set_xticks([])
ax.set_yticks([])

# Display
plt.tight_layout()
plt.savefig("/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231225-122818_25.png")
plt.close()