
import matplotlib.pyplot as plt
import numpy as np

# set figure size
plt.figure(figsize=(12, 8))

# create data
country = ['USA', 'UK', 'Germany', 'France']
startups = [200, 140, 130, 120]
funding = [4.5, 3.2, 2.7, 2.1]

# plot
ax = plt.subplot()
ax.bar(country, startups, 0.4, color='b', label='Startups')
ax.bar(country, funding, 0.4, bottom=startups, color='darkorange', label='Funding')

# set title
plt.title('Startups and funding in four countries in 2021', fontsize=16)

# set legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=2, fancybox=True, shadow=True)

# set xticks
ax.set_xticks(country)
ax.set_xticklabels(country, rotation=45, fontsize=12, wrap=True)

# resize image
plt.tight_layout()

# save image
plt.savefig(r'bar chart/png/180.png')

# clear current image state
plt.clf()