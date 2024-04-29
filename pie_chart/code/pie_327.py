
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

labels = ['YouTube', 'Instagram', 'Twitter', 'Facebook', 'TikTok', 'Reddit', 'Twitch']
sizes = [30, 20, 10, 20, 10, 5, 5]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffd6cc','#cc99ff','#ccccff']

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',startangle=90)
ax.axis('equal')

red_patch = mpatches.Patch(color='#ff9999', label='YouTube')
blue_patch = mpatches.Patch(color='#66b3ff', label='Instagram')
green_patch = mpatches.Patch(color='#99ff99', label='Twitter')
yellow_patch = mpatches.Patch(color='#ffcc99', label='Facebook')
pink_patch = mpatches.Patch(color='#ffd6cc', label='TikTok')
purple_patch = mpatches.Patch(color='#cc99ff', label='Reddit')
lightblue_patch = mpatches.Patch(color='#ccccff', label='Twitch')

plt.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch, pink_patch, purple_patch, lightblue_patch], bbox_to_anchor=(1.05, 1), loc='upper left')

plt.title('Social Media Platforms Usage in the US, 2021')
plt.tight_layout()
plt.xticks(rotation=45)

plt.savefig('pie chart/png/432.png')
plt.clf()