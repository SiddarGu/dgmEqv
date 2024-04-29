
import matplotlib.pyplot as plt
import numpy as np

# set data
month = ['January', 'February', 'March', 'April', 'May', 'June']
prod_a = [20000, 21000, 22000, 22000, 22000, 22000]
prod_b = [30000, 28000, 30000, 29000, 31000, 30000]
prod_c = [25000, 25500, 25000, 25500, 24000, 26000]

# plot figure
plt.figure(figsize=(7, 5))
ax = plt.subplot()
ax.plot(month, prod_a, label='Production A (units)', marker='o')
ax.plot(month, prod_b, label='Production B (units)', marker='o')
ax.plot(month, prod_c, label='Production C (units)', marker='o')
ax.set_title('Monthly Production of three types of products in 2021')
ax.set_xticks(np.arange(len(month)))
ax.set_xticklabels(month)
ax.legend(loc='best')
plt.tight_layout()

# label the value of each data point directly on the figure
for i in range(len(month)):
    ax.annotate(str(prod_a[i]), xy=(i, prod_a[i]), xytext=(i, prod_a[i] + 1000))
    ax.annotate(str(prod_b[i]), xy=(i, prod_b[i]), xytext=(i, prod_b[i] + 1000))
    ax.annotate(str(prod_c[i]), xy=(i, prod_c[i]), xytext=(i, prod_c[i] + 1000))

# save image
plt.savefig('line chart/png/517.png')

# clear figure
plt.close()