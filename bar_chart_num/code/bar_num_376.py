
import matplotlib.pyplot as plt
import numpy as np

# data
country = ['USA', 'UK', 'Germany', 'France']
manufacturing_cost = [400, 350, 300, 250]
production_output = [800, 750, 700, 650]

# create figure
fig, ax = plt.subplots(figsize=(10, 5))

# plot bar
ax.bar(country, manufacturing_cost, label='Manufacturing Cost(million)', color='#ff3f3f', bottom=0)
ax.bar(country, production_output, label='Production Output(million)', color='#3f9fff', bottom=manufacturing_cost)

# xticks
plt.xticks(country)

# show values
for i, v in enumerate(manufacturing_cost):
    ax.text(i - 0.1, v + 40, str(v), color='#ff3f3f', fontsize=12, fontweight='bold')
for i, v in enumerate(production_output):
    ax.text(i - 0.1, v + 40, str(v), color='#3f9fff', fontsize=12, fontweight='bold')

# title
ax.set_title('Manufacturing Cost and Production Output of four countries in 2021')

# legend
ax.legend(loc='upper left')

# tight layout and save
plt.tight_layout()
plt.savefig('Bar Chart/png/196.png')

# clear figure
plt.clf()