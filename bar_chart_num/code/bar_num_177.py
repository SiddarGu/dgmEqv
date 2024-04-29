
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()
width = 0.25

x_labels = np.arange(4)
business_a = [2000,3000,4000,5000]
business_b = [4000,5000,6000,7000]
business_c = [6000,7000,8000,9000]

ax.bar(x_labels, business_a, width, label='Business A')
ax.bar(x_labels + width, business_b, width, label='Business B')
ax.bar(x_labels + 2 * width, business_c, width, label='Business C')

ax.set_xticks(x_labels + width)
ax.set_xticklabels(['Q1', 'Q2', 'Q3', 'Q4'])
ax.legend(loc='upper right')
ax.set_title('Financial performance of three businesses from Q1 to Q4 2021')

for i in range(len(business_a)):
    ax.annotate(business_a[i], xy=(x_labels[i] + width/2, business_a[i]), ha='center', va='bottom')
for i in range(len(business_b)):
    ax.annotate(business_b[i], xy=(x_labels[i] + width/2, business_b[i]+business_a[i]), ha='center', va='bottom')
for i in range(len(business_c)):
    ax.annotate(business_c[i], xy=(x_labels[i] + width/2, business_c[i]+business_b[i]+business_a[i]), ha='center', va='bottom')

fig.set_size_inches(14, 8)
plt.tight_layout()
plt.savefig('Bar Chart/png/248.png')
plt.clf()