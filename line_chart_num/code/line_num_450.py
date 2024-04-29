
import matplotlib.pyplot as plt
import numpy as np

# Setting figure parameters
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

# Data
months = ['January', 'February', 'March', 'April', 'May']
sugar = [1000, 1200, 1300, 1400, 1200]
coffee = [500, 400, 450, 500, 550]
tea = [200, 250, 300, 350, 400]

# Plotting line chart
ax.plot(months, sugar, 'b-o', label='Sugar Consumption(lbs)')
ax.plot(months, coffee, 'r--s', label='Coffee Consumption(cups)')
ax.plot(months, tea, 'g-^', label='Tea Consumption(cups)')

# Labeling
ax.set_title('Average Monthly Consumption of Sugar, Coffee, and Tea in the US Food and Beverage Industry')
ax.set_xlabel('Month')
ax.set_xticks(np.arange(len(months)))
ax.set_xticklabels(months, rotation=45,  wrap=True)
ax.set_ylabel('Consumption')
ax.legend(loc='upper left')

# Adding data labels
for i, txt in enumerate(sugar):
    ax.annotate(txt, (months[i], sugar[i]))
for i, txt in enumerate(coffee):
    ax.annotate(txt, (months[i], coffee[i]))
for i, txt in enumerate(tea):
    ax.annotate(txt, (months[i], tea[i]))

# Automatically resizes the image by tight_layout()
plt.tight_layout()

# Saving image
plt.savefig('line chart/png/370.png')

# Clear the current image state
plt.clf()