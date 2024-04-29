
import matplotlib.pyplot as plt
import numpy as np

# Generate data
data = {'Country': ['USA', 'UK', 'Germany', 'France'], 
        'Literature': [400, 420, 370, 390], 
        'History': [300, 280, 320, 340], 
        'Philosophy': [200, 220, 250, 230]}

countries = np.arange(len(data['Country']))

# Set up chart
plt.figure(figsize=(15, 7)) 
ax = plt.subplot()

# Set up variables
literature = data['Literature']
history = data['History']
philosophy = data['Philosophy']

# Plot data
bar_literature = ax.bar(countries, literature, width=0.6, label='Literature')
bar_history = ax.bar(countries, history, bottom=literature, width=0.6, label='History')
bar_philosophy = ax.bar(countries, philosophy, bottom=np.array(literature)+np.array(history), width=0.6, label='Philosophy')

# Set up labels
ax.set_xticks(countries)
ax.set_xticklabels(data['Country'])
plt.title('Number of publications in social sciences and humanities in four countries in 2021')
ax.legend()

# Add labels to each bar
for bar_literature, bar_history, bar_philosophy in zip(bar_literature, bar_history, bar_philosophy):
    ax.annotate(str(bar_literature.get_height()), xy=(bar_literature.get_x() + bar_literature.get_width() / 2, bar_literature.get_height()), 
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate(str(bar_history.get_height()), xy=(bar_history.get_x() + bar_history.get_width() / 2, bar_literature.get_height() + bar_history.get_height()), 
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom')
    ax.annotate(str(bar_philosophy.get_height()), xy=(bar_philosophy.get_x() + bar_philosophy.get_width() / 2, bar_literature.get_height() + bar_history.get_height() + bar_philosophy.get_height()), 
                xytext=(0, 3), textcoords="offset points",
                ha='center', va='bottom')

# Autoresize
plt.tight_layout()

# Save
plt.savefig('Bar Chart/png/42.png')

# Clear
plt.clf()