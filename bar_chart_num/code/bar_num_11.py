
import matplotlib.pyplot as plt
import numpy as np

country = ['USA','UK','Germany','France']
football_fans = [3500,4000,4700,4400]
tennis_fans = [3000,2500,2300,2700]
basketball_fans = [4500,3700,4200,3800]

x = np.arange(len(country)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(x, football_fans, width, label='Football Fans')
ax.bar(x + width, tennis_fans, width, label='Tennis Fans')
ax.bar(x + (width * 2), basketball_fans, width, label='Basketball Fans')

ax.set_ylabel('Number of Fans')
ax.set_title('Number of Fans for Football, Tennis and Basketball in four countries in 2021')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(country)

ax.legend(loc='best')
ax.autoscale_view()

for x_pos, y_pos, y_val in zip(x, football_fans, football_fans):
    label = "{:.1f}".format(y_val)
    ax.annotate(label, (x_pos, y_pos), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')

for x_pos, y_pos, y_val in zip(x, tennis_fans, tennis_fans):
    label = "{:.1f}".format(y_val)
    ax.annotate(label, (x_pos + width, y_pos), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')

for x_pos, y_pos, y_val in zip(x, basketball_fans, basketball_fans):
    label = "{:.1f}".format(y_val)
    ax.annotate(label, (x_pos + width * 2, y_pos), xytext=(0,5), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('Bar Chart/png/550.png')
plt.clf()