
import matplotlib.pyplot as plt
import numpy as np

# Data
Platform = ['Facebook','Instagram','Twitter','TikTok','Snapchat','YouTube']
Users = [500, 400, 200, 400, 100, 900]
Country = ['USA']*6

# Plot
fig, ax = plt.subplots(figsize=(14,7))
ax.bar(Platform, Users, color='#66a8e7')
ax.set_xticklabels(Platform, rotation=45, ha="right", fontsize=15)
ax.set_title('Number of users on social media platforms in the USA in 2021', fontsize=20)
ax.set_xlabel('Platform', fontsize=15)
ax.set_ylabel('Users (million)', fontsize=15)
ax.set_ylim(0, 1000)
plt.xticks(np.arange(len(Platform)), Platform)
ax.legend(Country, fontsize=15)
plt.tight_layout()
plt.savefig('bar chart/png/156.png')
plt.clf()