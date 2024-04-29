
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.figure(figsize=(8,8))

data = [35,20,20,15,10]
labels = ['Television','Social Media','Streaming Services','Radio','Print Media']

plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')

red_patch = mpatches.Patch(color='red', label='Television')
blue_patch = mpatches.Patch(color='blue', label='Social Media')
green_patch = mpatches.Patch(color='green', label='Streaming Services')
orange_patch = mpatches.Patch(color='orange', label='Radio')
purple_patch = mpatches.Patch(color='purple', label='Print Media')

plt.legend(handles=[red_patch, blue_patch, green_patch, orange_patch, purple_patch], bbox_to_anchor=(1.1, 1.05))
plt.title('Popularity of Media Platforms among Sports and Entertainment Fans in 2023', fontsize=15, wrap=True)

plt.tight_layout()
plt.savefig('pie chart/png/83.png')

plt.clf()