
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

# Set data
data = [[2001,500,450,400],
        [2002,550,420,390],
        [2003,600,400,380],
        [2004,650,430,410]]

# Convert data into numpy array
data = np.array(data)
x = data[:, 0]
y_house = data[:, 1]
y_apartment = data[:, 2]
y_condominium = data[:, 3]

# Draw line chart
ax.plot(x, y_house, color='green', linewidth=2, label='House')
ax.plot(x, y_apartment, color='red', linewidth=2, label='Apartment')
ax.plot(x, y_condominium, color='blue', linewidth=2, label='Condominium')

# Set xticks
ax.set_xticks(x)

# Annotate data point
for i, j in enumerate(y_house):
    ax.annotate(str(j), xy=(x[i], j + 5), fontsize=12)
for i, j in enumerate(y_apartment):
    ax.annotate(str(j), xy=(x[i], j + 5), fontsize=12)
for i, j in enumerate(y_condominium):
    ax.annotate(str(j), xy=(x[i], j + 5), fontsize=12)

# Add title
ax.set_title('Average House, Apartment and Condominium Prices in US from 2001 to 2004',
             fontsize=20, wrap=True)

# Add legend
ax.legend(loc='upper left', fontsize=12)

# Adjust layout
plt.tight_layout()

# Save and clear figure
plt.savefig('line chart/png/82.png')
plt.clf()