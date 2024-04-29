
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize = (12,8))
ax = fig.add_subplot(1,1,1)

# Set data
types = ['Concerts', 'Exhibitions', 'Theater', 'Festivals']
events = [30, 50, 25, 20]
participants = [5000, 9000, 4000, 8000]

# Plot
ax.bar(types, events, width=0.35, bottom=0, color='#FFA500', label="Events")
ax.bar(types, participants, width=0.35, bottom=0, color='#EEC900', label="Participants")

# Set x ticks and rotate labels
ax.set_xticks(np.arange(len(types)))
ax.set_xticklabels(types, rotation=45, ha="right", wrap=True)

# Set legend
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.05), ncol=2)

# Set title
ax.set_title('Number of Events and Participants in Arts and Culture in 2021')

# Fit figure and save
fig.tight_layout()
fig.savefig('bar chart/png/550.png')
plt.clf()