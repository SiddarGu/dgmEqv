
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(10, 5))
ax = plt.subplot()
Region = ['Asia','Europe','North America','South America']
Hotels = [500, 800, 700, 600]
Restaurants = [2000,2300,2500,2200]
Tourists = [3000,4000,3500,3800]
width = 0.2 
ax.bar(Region, Hotels, width, label='Hotels', color='green')
ax.bar(np.arange(len(Region))+width, Restaurants, width, label='Restaurants', color='blue')
ax.bar(np.arange(len(Region))+2*width, Tourists, width, label='Tourists', color='red')

ax.set_title('Number of hotels, restaurants, and tourists in four regions in 2021')
ax.set_xticks(np.arange(len(Region))+width)
ax.set_xticklabels(Region, rotation=45, fontsize='small')
ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('bar chart/png/493.png')
plt.clf()