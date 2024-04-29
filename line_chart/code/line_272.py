
import matplotlib.pyplot as plt
import numpy as np

# set up figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot()

# get data
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
social_media_usage = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400]
web_usage = [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200]

# plot data
ax.plot(month, social_media_usage, label='Social Media Usage')
ax.plot(month, web_usage, label='Web Usage')

# set up labels
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Usage', fontsize=14)
ax.set_title('Social media and web usage from January to August 2021', fontsize=16)

# set up legend
ax.legend(loc='best', fontsize=12, frameon=True, shadow=True)
ax.grid(color='#DDDDDD', linestyle='-', linewidth=1)

# set up xticks
ax.set_xticks(np.arange(len(month)), minor=False)
ax.set_xticklabels(month, rotation=90, fontsize=12)

# resize figure
plt.tight_layout()

# save figure
plt.savefig('line chart/png/62.png')

# clear state
plt.clf()