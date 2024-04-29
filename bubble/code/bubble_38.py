
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize

# Correcting the bubble chart for the Maximizing Tourism Revenue and Satisfaction

# Data
countries = ["USA", "Japan", "UK", "France", "Italy"]
average_spending = np.array([3000, 4000, 2500, 2000, 3500])  # Average Spending (USD)
tourist_arrivals = np.array([72, 45, 60, 68, 55])  # Tourist Arrivals (Millions)
satisfaction_score = np.array([90, 87, 85, 83, 80])  # Satisfaction Score
tourism_contribution = np.array([25, 20, 30, 15, 10])  # Tourism Contribution (%)

# Create figure
fig, ax = plt.subplots(figsize=(14, 7))

# Color mapping and normalization
cmap = cm.get_cmap("Blues")
norm = plt.Normalize(vmin=min(tourism_contribution), vmax=max(tourism_contribution))
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Plotting the data
for country, spending, arrivals, satisfaction, contribution in zip(countries, average_spending, tourist_arrivals, satisfaction_score, tourism_contribution):
    size = (satisfaction - 80) * 1000 / 10 + 600
    color = cmap(norm(contribution))
    ax.scatter(spending, arrivals, s=size, color=color, alpha=0.6, edgecolor='black', label=None)
    ax.scatter([], [], color=color, label=country + f'{satisfaction}', s=20)

# Legend and color bar
ax.legend(title='Satisfaction Score', loc="upper right")
cbar = fig.colorbar(sm, ax=ax, fraction=0.1, pad=0.05, aspect=20)
cbar.set_label('Tourism Contribution (%)')

# Labels, grid, and title
ax.grid(True, linestyle="-.", color="black", alpha=0.3)
ax.set_xlabel('Average Spending (USD)')
ax.set_ylabel('Tourist Arrivals (Millions)')
ax.set_title("Maximizing Tourism Revenue and Satisfaction - Tourism and Hospitality 2023")

# Adjust layout and save the figure
plt.tight_layout()
# The image must be saved as /cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/1.png.
plt.savefig("/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/1.png")

# Clear the current image state at the end of the code.
plt.cla()