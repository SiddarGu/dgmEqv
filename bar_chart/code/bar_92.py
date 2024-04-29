
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

# Data
activities = ['Football', 'Basketball', 'Tennis', 'Golf']
participants = [1.5, 2.0, 1.2, 0.8]
spectators = [2.5, 3.0, 2.3, 1.5]

# Plot
x_indexes = np.arange(len(activities))
width = 0.35
ax.bar(x_indexes - width/2, participants, width, label='Participants')
ax.bar(x_indexes + width/2, spectators, width, label='Spectators')

# Settings
ax.set_title('Number of participants and spectators in four sports activities in 2021')
ax.set_xticks(x_indexes)
ax.set_xticklabels(activities, rotation=45, wrap=True)
ax.legend()

# Save
plt.tight_layout()
plt.savefig('bar chart/png/55.png')

# Clear
plt.clf()