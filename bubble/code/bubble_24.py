import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

# Data for the popularity and financial status of sports and entertainment activities
popularity_scores = np.array([90, 85, 80, 75, 70, 65])  # Popularity (Score)
revenue = np.array([70, 60, 50, 40, 30, 25])  # Revenue (Billion $)
participants = np.array([2.5, 2, 1.5, 1, 0.5, 0.2])  # Participants (Millions)
safety_scores = np.array([80, 75, 70, 65, 60, 50])  # Safety (Score)

# Line labels
line_labels = [f"{popularity} {participants}" for popularity, participants in zip(['Basketball', 'Football', 'Cricket', 'Tennis', 'Swimming', 'Skiing'], participants)]

# Create figure
fig, ax = plt.subplots(figsize=(15, 10))

# Color mapping and normalization
cmap = plt.cm.get_cmap('RdYlGn')
norm = Normalize(vmin=min(safety_scores), vmax=max(safety_scores))
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

# Plotting the data
for line_label, popularity, rev, participant, safety in zip(line_labels, popularity_scores, revenue, participants, safety_scores):
    bubble_size = participant * 400 + 60
    color = cmap(norm(safety))
    ax.scatter(popularity, rev, s=bubble_size, color=color, alpha=0.6, edgecolor='black', label=None)
    ax.scatter([], [], s=20, color=color, label=line_label)

# Legend and color bar
ax.legend(title='Participants (Millions)', bbox_to_anchor=(0.9, 0.5))
cbar = fig.colorbar(sm, ax=ax, orientation='vertical')
cbar.set_label('Safety (Score)')

# Labels and title
ax.set_xlabel('Popularity (Score)')
ax.set_ylabel('Revenue (Billion $)')
ax.set_title('Popularity and Financial Status of Sports and Entertainment Activities')

# Grid and layout adjustment
ax.grid(True)
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/7_2023122261326.png')

plt.clf()