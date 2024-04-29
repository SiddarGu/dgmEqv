
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
country = np.array(['USA','UK','Germany','France'])
sports_events = np.array([20,25,18,23])
entertainment_events = np.array([30,35,32,37])

x = np.arange(len(country))
width = 0.35

ax.bar(x - width/2, sports_events, width, color='#FF9800', label="Sports Events")
ax.bar(x + width/2, entertainment_events, width, color='#2196F3', label="Entertainment Events")
ax.set_xticks(x)
ax.set_xticklabels(country, rotation=45, va="top", ha="right", wrap=True)
ax.set_title('Number of sports and entertainment events in four countries in 2021')
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/47.png')
plt.clf()