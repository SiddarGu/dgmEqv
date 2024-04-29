
import matplotlib.pyplot as plt
import numpy as np

#Prepare data
month = ['Jan','Feb','Mar','Apr','May','Jun','Jul']
usersA = [1000, 1200, 800, 1500, 1000, 1200, 1300]
usersB = [800, 900, 1100, 1200, 1400, 1500, 1400]
usersC = [1200, 1100, 1300, 1400, 1600, 1800, 1700]

#Create figure
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(1,1,1)

#Plot
ax.plot(month, usersA, 'r-', label = 'Users A')
ax.plot(month, usersB, 'b-', label = 'Users B')
ax.plot(month, usersC, 'g-', label = 'Users C')

#Title
plt.title('Monthly user growth of three social media platforms in 2021')

#Set xticks
ax.set_xticks(np.arange(7))
ax.set_xticklabels(month, rotation = 45, ha='right')

#Legend
ax.legend(loc = 'best')
plt.tight_layout()
plt.savefig('line chart/png/340.png')

#Clear the current image state at the end of the code
plt.clf()