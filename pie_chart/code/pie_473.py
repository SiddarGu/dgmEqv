
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# setting figure size
fig = plt.figure(figsize=(7,7))

# plotting pie chart
ax = fig.add_subplot(111)
labels=['Monetary Donations','In-kind Donations','Volunteering Time','Gift of Stock']
values= [50,25,15,10]
ax.pie(values,labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12})

# setting title
ax.set_title('Types of Donations to Nonprofit Organizations in the USA,2023')

# setting legend
donation_type = mpatches.Patch(color='white', label='Donation Type')
ax.legend(handles=[donation_type], loc="upper right")

# setting font
plt.rcParams["font.family"] = 'sans-serif'
plt.rcParams["font.sans-serif"] = 'Arial'

# setting rotation for labels
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

# setting image to show
plt.tight_layout()

# saving figure
plt.savefig('pie chart/png/13.png')

# clearing current image state
plt.clf()