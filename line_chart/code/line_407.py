
import matplotlib.pyplot as plt
import numpy as np

# Create data
x=np.array([2001,2002,2003,2004])
y1=np.array([20000,25000,30000,33000])
y2=np.array([10000,11000,12000,14000])
y3=np.array([5000,6000,7000,8000])

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Plot line
ax.plot(x, y1, color='b', marker='o',label='Number of Cases')
ax.plot(x, y2, color='r', marker='o',label='Number of Trials')
ax.plot(x, y3, color='g', marker='o',label='Number of Judgements')

# Customize axis
ax.set_xlabel('Year')
ax.set_ylabel('Number')
ax.set_title('Legal Cases in the U.S. from 2001-2004')
ax.legend(loc='upper right')
ax.set_xticks(x)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/445.png')

# Clear the current image state
plt.clf()