
import matplotlib.pyplot as plt
import numpy as np

country = ['USA', 'UK', 'Germany', 'France']
internet_users = [300, 50, 80, 40]
social_media_users = [280, 45, 75, 35]

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot bars
ax.bar(country, internet_users, width=0.5, label='Internet Users', bottom=social_media_users)
ax.bar(country, social_media_users, width=0.5, label='Social Media Users')

# Set title
ax.set_title('Number of Internet and Social Media Users in Four Countries in 2021')

# Customize legend position
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=2)

# Add value label
for x, y in zip(country, internet_users):
    ax.annotate(str(y), xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')

for x, y in zip(country, social_media_users):
    ax.annotate(str(y), xy=(x, y), xytext=(0, 5), textcoords='offset points', ha='center', va='top')

# Resize the figure
fig.tight_layout()

# Set xticks
plt.xticks(country, country, rotation='vertical')

# Save figure
plt.savefig('Bar Chart/png/116.png')

# Clear the current image state
plt.cla()