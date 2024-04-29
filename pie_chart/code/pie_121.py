
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# create figure and set size
fig = plt.figure(figsize=(12, 8))

# create data list
causes = ['Education', 'Healthcare', 'Environment', 'Poverty', 'Humanity']
percentage = [20, 30, 25, 15, 10]

# create pie chart
plt.pie(percentage, labels=causes, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 14}, wedgeprops={'linewidth': 0.5})

# set legend
green_patch = mpatches.Patch(color='green', label='Education')
blue_patch = mpatches.Patch(color='blue', label='Healthcare')
yellow_patch = mpatches.Patch(color='yellow', label='Environment')
pink_patch = mpatches.Patch(color='pink', label='Poverty')
black_patch = mpatches.Patch(color='black', label='Humanity')
plt.legend(handles=[green_patch, blue_patch, yellow_patch, pink_patch, black_patch], loc='upper left', fontsize=14)

# set title
plt.title('Charitable Donation Distribution in the USA, 2023', fontsize=18)

# adjust the plot
plt.xticks(rotation=30)
plt.tight_layout()

# save the figure
plt.savefig('pie chart/png/36.png')

# clear the current figure
plt.clf()