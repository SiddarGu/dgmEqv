
import matplotlib.pyplot as plt
import numpy as np

#Data
state = np.array(['California', 'New York', 'Texas', 'Florida'])
Retail_Stores = np.array([400,350,500,450])
Online_Stores = np.array([700,650,850,750])

# Create figure
fig = plt.figure()
ax = fig.add_subplot()

# Plotting
p1=ax.bar(state, Retail_Stores, color='#2b7bba', label='Retail Stores')
p2=ax.bar(state, Online_Stores, bottom=Retail_Stores, color='#7bb274', label='Online Stores')

# Adjusting the code
ax.set_xticks(state)
ax.set_xticklabels(state, rotation=90)
fig.tight_layout()

# Adding Legend
ax.legend(loc='upper left')

# Adding Title
ax.set_title('Number of retail stores and online stores in four states in 2021')

# Annotate
for i, j in enumerate(Retail_Stores):
    ax.annotate(str(j), xy=(state[i], j/2), ha='center', va='center')

for i, j in enumerate(Online_Stores):
    ax.annotate(str(j), xy=(state[i], j/2+Retail_Stores[i]), ha='center', va='center')

# Save figure
plt.savefig('Bar Chart/png/427.png', format='png')

# Clear
plt.clf()