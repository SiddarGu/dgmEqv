
import matplotlib.pyplot as plt
import numpy as np

# Set up data
year = np.array([2001, 2002, 2003, 2004])
donA = np.array([1000, 1200, 800, 1500])
donB = np.array([800, 900, 1100, 1200])
donC = np.array([1200, 1100, 1300, 1400])
donD = np.array([1500, 1600, 1200, 800])

# Create chart
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot()
ax.plot(year, donA, label='Donation A(million dollars)', linewidth=3)
ax.plot(year, donB, label='Donation B(million dollars)', linewidth=3)
ax.plot(year, donC, label='Donation C(million dollars)', linewidth=3)
ax.plot(year, donD, label='Donation D(million dollars)', linewidth=3)
ax.tick_params(axis='both', labelsize=13)
ax.set_title('Donations in four categories of nonprofit organizations')

# Annotate
for x, y in zip(year, donA):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), textcoords='offset points', xytext=(0,5), ha='center')
for x, y in zip(year, donB):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), textcoords='offset points', xytext=(0,5), ha='center')
for x, y in zip(year, donC):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), textcoords='offset points', xytext=(0,5), ha='center')
for x, y in zip(year, donD):
    ax.annotate('{:.0f}'.format(y), xy=(x, y), textcoords='offset points', xytext=(0,5), ha='center')

# Add legend
ax.legend(loc='upper left')

# Set xticks
plt.xticks(np.arange(year.min(), year.max()+1, 1))

# Resize image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/393.png')

# Clear image
plt.clf()