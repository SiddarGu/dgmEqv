
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,5))

platforms = ('Facebook','Twitter','Instagram','YouTube')
users = np.array([2.8,1.2,1.5,2.5])
time_spent = np.array([3,2,1,4])

ax = plt.subplot()
ax.set_title('Social media usage and time spent on four platforms in 2021')
ax.bar(platforms, users, label='Users (million)')
ax.bar(platforms, time_spent, bottom=users, label='Time Spent')
ax.set_ylabel('Usage (million)')
ax.set_xticklabels(platforms, rotation=45, ha='right', wrap=True)
ax.legend()

plt.tight_layout()
plt.savefig('bar chart/png/240.png')
plt.clf()