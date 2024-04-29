
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April', 'May', 'June']
rest_a = [50, 60, 45, 55, 65, 60]
rest_b = [40, 45, 50, 40, 48, 43]
rest_c = [30, 35, 27, 32, 37, 40]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

ax.plot(month, rest_a, marker='o', label='Restaurant A')
ax.plot(month, rest_b, marker='o', label='Restaurant B')
ax.plot(month, rest_c, marker='o', label='Restaurant C')

for a,b,c in zip(month, rest_a, rest_b):
    ax.annotate(str(b), xy=(a,b), xytext=(5,-5), textcoords='offset points')
    ax.annotate(str(c), xy=(a,c), xytext=(-25,-5), textcoords='offset points')

ax.legend(loc='best', fontsize=12)
ax.set_title('Monthly Sales of Three Restaurants in 2021', fontsize=14)
ax.set_xlabel('Month', fontsize=14)
ax.set_ylabel('Sales (million dollars)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('line chart/png/550.png', bbox_inches='tight')
plt.clf()