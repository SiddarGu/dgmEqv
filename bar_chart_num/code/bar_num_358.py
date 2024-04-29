
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Create bar chart
organizations = ['Red Cross', 'World Vision', 'UNICEF', 'Habitat for Humanity']
donations = [3000, 2000, 2500, 1000]
hours = [100, 140, 90, 120]

x = np.arange(len(organizations)) 
width = 0.35 

ax.bar(x - width/2, donations, width, label='Donations (thousand $)')
ax.bar(x + width/2, hours, width, label='Volunteer Hours (thousand)')

# Labels
ax.set_ylabel('Amount')
ax.set_title('Amount of donations and volunteer hours by four nonprofit organizations in 2021')
ax.set_xticks(x)
ax.set_xticklabels(organizations)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2)

# Annotate
for i in range(len(organizations)):
    ax.annotate(str(donations[i])+', '+str(hours[i]), (x[i]-width/2-0.05, donations[i]/2+hours[i]/2), fontsize=12)

# Resize 
fig.tight_layout()

# Save
plt.savefig('Bar Chart/png/522.png')

# Clear the current image state
plt.clf()