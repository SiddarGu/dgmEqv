
import matplotlib.pyplot as plt 
import numpy as np

# Create a figure object
fig = plt.figure(figsize=(15, 8))

# Adding subplot to the figure object
ax = fig.add_subplot(1, 1, 1)

# Defining labels
states = ['California', 'New York', 'Texas', 'Florida']
criminal_cases = np.array([3000, 3200, 3500, 4000])
civil_cases = np.array([5000, 4200, 4500, 4800])

# Setting the position of the x-axis ticks
x_pos = np.arange(len(states))

# Plotting the Bar Chart
ax.bar(x_pos, criminal_cases, color='#38b6ff', label='Criminal Cases')
ax.bar(x_pos, civil_cases, color='#ffd938', bottom=criminal_cases, label='Civil Cases')

# Adding legend
ax.legend(loc="upper right")

# Setting the xticks
ax.set_xticks(x_pos)
ax.set_xticklabels(states)

# Adding title
ax.set_title('Number of criminal and civil cases in four states in 2021')

# Adding Value Labels
for a,b,c in zip(x_pos, criminal_cases, civil_cases): 
    ax.annotate(str(b), (a, b+0.2), fontsize=10)
    ax.annotate(str(c), (a, c+b+0.2), fontsize=10)

# Automatically adjusting the image size
plt.tight_layout()

# Saving the figure
plt.savefig("Bar Chart/png/327.png") 

# Clearing the figure
plt.clf()