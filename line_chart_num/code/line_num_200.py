
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

# Set data
year = [2012, 2013, 2014, 2015, 2016]
social_media_users = [500, 800, 1000, 1500, 2000]
online_shopping_users = [300, 400, 500, 700, 1000]
time_spent_social_media = [2,3,3.5,4,4.5]

# Plot line chart
ax.plot(year,social_media_users,label="Social Media Users (Millions)")
ax.plot(year,online_shopping_users,label="Online Shopping Users (Millions)")
ax.plot(year,time_spent_social_media,label="Time Spent on Social Media")

# Set xticks
plt.xticks(year,rotation=45)

# Set legend and title
ax.legend(loc='best', fontsize='small', ncol=2, frameon=True, shadow=True, fancybox=True)
plt.title("Growth of Social Media and Online Shopping Usage from 2012-2016", fontsize=15, wrap=True)

# add annotation
for a,b,c in zip(year,social_media_users,online_shopping_users):
    ax.annotate('%s' %b,xy=(a,b), xytext=(-2,4),textcoords='offset points')
    ax.annotate('%s' %c,xy=(a,c), xytext=(-2,4),textcoords='offset points')

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/562.png')

# Clear current image state
plt.clf()