
import matplotlib.pyplot as plt
import numpy as np

data = [['January', 15, 1000], ['February', 14, 1100], ['March', 17, 800], ['April', 19, 1100], ['May', 20, 1200], ['June', 18, 1000], ['July', 17, 900], ['August', 20, 1200], ['September', 19, 1000], ['October', 15, 900], ['November', 14, 1000], ['December', 15, 1100]]
months = [row[0] for row in data]
num_tourists = [row[1] for row in data]
avg_spending = [row[2] for row in data]

fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(111) 
ax1.plot(months, num_tourists, label='Number of Tourists')
ax1.plot(months, avg_spending, label='Average Spending')
ax1.grid(linestyle='--', color='gray', linewidth=0.5)
ax1.set_title('Monthly Tourist Visits and Spending in the US in 2021')
ax1.set_xlabel('Months')
ax1.set_ylabel('Number of Tourists (millions) & Average Spending (dollars)')
ax1.annotate('Max Tourists: 20', xy=(4.8, 20.2), xytext=(4.8, 20.2), fontsize=10)
ax1.annotate('Max Spending: 1200', xy=(8.8, 1202), xytext=(8.8, 1202), fontsize=10)
ax1.tick_params(axis='x', rotation=90, labelsize=10)
ax1.legend()
plt.xticks(np.arange(12), months, rotation=90)
plt.tight_layout()
plt.savefig('line chart/png/565.png', bbox_inches='tight', dpi=600)
plt.clf()