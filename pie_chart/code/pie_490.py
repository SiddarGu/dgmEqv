
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# create figure with larger size
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot()

# create list for labels and market share
labels = ['Television','Digital','Radio','Print','Out of Home']
share = [40,30,15,10,5]

# set color for each label
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6']

# plot pie chart
ax.pie(share, labels=labels, colors=colors, startangle=90, autopct='%.1f%%',textprops={'fontsize': 14})

# make chart look better
ax.set_title('Market Share of Media Platforms in the USA, 2023', fontsize=20)
ax.axis('equal')

# legend
television_patch = mpatches.Patch(color='#ff9999', label='Television')
digital_patch = mpatches.Patch(color='#66b3ff', label='Digital')
radio_patch = mpatches.Patch(color='#99ff99', label='Radio')
print_patch = mpatches.Patch(color='#ffcc99', label='Print')
outhome_patch = mpatches.Patch(color='#ffb3e6', label='Out of Home')

plt.legend(handles=[television_patch, digital_patch, radio_patch, print_patch, outhome_patch], bbox_to_anchor=(1,0.5))

# automatically resize the image 
fig.tight_layout()

# save the figure
plt.savefig('pie chart/png/455.png', dpi=200)

# clear the current image state
plt.clf()