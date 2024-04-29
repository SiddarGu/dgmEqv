
import matplotlib.pyplot as plt
import numpy as np

# Set data
Year = [2012,2013,2014,2015]
Computer_Owners = [100, 110, 120, 130]
Smartphone_Owners = [200, 230, 260, 290]
Internet_Users = [300, 330, 360, 390]

# Create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

# Plot data
bar_width = 0.25
xlocs = np.arange(len(Computer_Owners))
ax.bar(xlocs-bar_width, Computer_Owners, width=bar_width, color='b', label='Computer Owners')
ax.bar(xlocs, Smartphone_Owners, width=bar_width, color='g', label='Smartphone Owners')
ax.bar(xlocs+bar_width, Internet_Users, width=bar_width, color='r', label='Internet Users')

# Labels and titles
ax.set_title('Number of technology owners and internet users from 2012 to 2015')
ax.set_xlabel('Year')
ax.set_ylabel('Number')
ax.set_xticks(ticks=xlocs)
ax.set_xticklabels(labels=Year)
ax.legend()

# Annotate values
for Computer_Owner,Smartphone_Owner,Internet_User, xloc in zip(Computer_Owners,Smartphone_Owners,Internet_Users, xlocs):
    ax.annotate(Computer_Owner, xy=(xloc-bar_width, Computer_Owner+2), rotation=90)
    ax.annotate(Smartphone_Owner, xy=(xloc, Smartphone_Owner+2), rotation=90)
    ax.annotate(Internet_User, xy=(xloc+bar_width, Internet_User+2), rotation=90)

# Resize and save
fig.tight_layout()
plt.savefig('Bar Chart/png/576.png')
# Clear
plt.clf()