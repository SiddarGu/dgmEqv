
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

#data
country = ["USA","UK","Germany","France"]
internet_users = [300,150,200,120]
avg_time_spent = [4.5,3.9,4.2,3.6]

#plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.bar(country, internet_users, label="Internet Users (million)")
ax.bar(country, avg_time_spent, bottom=internet_users, label="Average Time Spent on the Internet (hours)")
ax.set_title("Internet usage and average time spent in four countries in 2021")
ax.set_xlabel("Country")
ax.legend(loc='upper right')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
for i, v in enumerate(internet_users):
    ax.text(i-0.2, v/2, str(v), color='white', fontweight='bold')
for i, v in enumerate(avg_time_spent):
    ax.text(i-0.2, internet_users[i]+v/2, str(v), color='white', fontweight='bold')
plt.tight_layout()
plt.xticks(np.arange(len(country)), country)
plt.savefig("Bar Chart/png/436.png")
plt.clf()