
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['axes.unicode_minus']=False

# Set up figure
fig = plt.figure(figsize=(16,10))
ax = fig.add_subplot()

# Data
month = ["January", "February", "March", "April", "May", "June", "July"]
percentage_A = [20,25,30,35,40,45,50]
percentage_B = [15,20,25,30,35,40,45]
percentage_C = [25,30,35,40,45,50,55]

# Plotting
plt.plot(month, percentage_A, label = 'Percentage of Users A')
plt.plot(month, percentage_B, label = 'Percentage of Users B')
plt.plot(month, percentage_C, label = 'Percentage of Users C')

# Labels and Titles
plt.title('Percentage Increase in Social Media Users from January to July 2021', fontsize=20)
plt.xlabel('Month', fontsize=15)
plt.ylabel('Percentage', fontsize=15)
plt.xticks(rotation=45, fontsize=15)
plt.yticks(fontsize=15)
plt.legend(loc='best', fontsize=15)

#Grid and tight layout
plt.grid(True)
plt.tight_layout()

# Save and clear
plt.savefig('line chart/png/336.png')
plt.clf()