
import matplotlib.pyplot as plt
import numpy as np

# Data
Country = np.array(['USA','UK','Germany','France'])
Internet_Users = np.array([350,90,80,70])
Social_Media_Users = np.array([300,80,75,65])

# Create figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)

# Plot
bar1 = ax.bar(Country, Internet_Users, label='Internet Users', color='b')
bar2 = ax.bar(Country, Social_Media_Users, bottom=Internet_Users, label='Social Media Users', color='g')

# Labels
plt.title('Number of Internet and Social Media Users in four countries in 2021')
plt.xticks(Country)
ax.set_ylabel('Number of Users (million)')
ax.set_xlabel('Countries')

# Legend
ax.legend()

# Annotate
for b1, b2 in zip(bar1, bar2):
    h1 = b1.get_height()
    h2 = b2.get_height()
    ax.annotate(str(h1), xy=(b1.get_x() + b1.get_width() / 2, h1), xytext=(0, 3), 
            textcoords="offset points", ha='center', va='bottom', color='white')
    ax.annotate(str(h2), xy=(b2.get_x() + b2.get_width() / 2, h1 + h2), xytext=(0, 3), 
            textcoords="offset points", ha='center', va='bottom', color='white')

# Adjust figure
plt.tight_layout()

# Save and clear
plt.savefig('Bar Chart/png/166.png')
plt.clf()